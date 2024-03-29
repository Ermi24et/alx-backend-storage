#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def url_access_count(method):
    """
    counts how many times a url is accessed
    """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """
    uses requests module to obtain the HTML content of a particular
    URL and returns it
    """
    url1 = requests.get(url)
    return url1.text
