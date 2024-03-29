#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import redis

store = redis.Redis()


def get_page(url: str) -> str:
    """
    uses requests module to obtain the HTML content of a particular
    URL and returns it
    """
    res = requests.get(url).text
    if not store.get(f"count:{url}"):
        store.set(f"count:{url}", 1)
        store.setex(f"res:{url}", 10, res)
    else:
        store.incr(f"count:{url}", 1)
    return res
