#!/usr/bin/env python3
"""
writing strings to redis
"""
import redis
import uuid
from typing import Union, Callable, Any


def count_calls(method: Callable) -> Callable:
    """
    decorator that takes a single method and returns callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """
        wrapper function that increments a key
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper

class Cache:
    """
    cache class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
    
    def get_str(self, key: str) -> str:
        """
        parametrize cache.get with the correct conversion function
        """
        return str(self._redis.get(key))
    
    def get_int(self, key: str) -> int:
        """
        parametrize cache.get with the correct conversion function
        """
        return int(self._redis.get(key))
