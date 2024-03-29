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
    result = requests.get(url).text
    if not store.get("count:{}".format(url)):
        store.set("count:{}".format(url), 1)
        store.setex("result:{}".format(url), 10, result)
    else:
        store.incr("count:{}".format(url), 1)
    return result
