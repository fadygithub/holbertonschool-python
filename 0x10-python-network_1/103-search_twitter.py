#!/usr/bin/python3
"""
    This will search 5 tweets
"""


import requests
from sys import argv
import base64


if __name__ == "__main__":
    c_key = argv[1]
    c_secret = argv[2]
    str_search = argv[3]
    headers = {}
    url = 'https://api.twitter.com/1.1/search/tweets.json?q='
    url += '{}&count=5'.format(str_search)
    header = {}
    req = requests.get(url, headers=header)
    for x in req.json():
        print("[{}] {} by {}".format(x.get("id"), x.get("text"), x.get("user").get("name")))
