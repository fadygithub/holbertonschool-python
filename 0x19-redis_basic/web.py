#!/usr/bin/env python3
"""Get_page implementation"""
from typing import KeysView
from redis.client import Redis
import requests


redis = Redis()
c = 0


def get_page(url: str) -> str:
    """
    returns html content of a URL
    """
    k = f"count:{url}"
    redis.set(k, c)
    resp = requests.get(url)
    redis.incr(k)
    redis.setex(KeysView, 10, redis.get(k))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
