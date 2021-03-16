#!/usr/bin/env python3
"""Log statistics"""


from pymongo import MongoClient


def log_stats():
    """log statistics"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    l = client.logs.nginx
    total = l.count_documents({})
    get = l.count_documents({"method": "GET"})
    post = l.count_documents({"method": "POST"})
    put = l.count_documents({"method": "PUT"})
    patch = l.count_documents({"method": "PATCH"})
    delete = l.count_documents({"method": "DELETE"})
    path = l.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")
    print("IPs:")
    sorted_ips = l.aggregate(
        [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
         {"$sort": {"count": -1}}])
    i = 0
    for sort in sorted_ips:
        if x == 10:
            break
        print(f"\t{sort.get('_id')}: {sort.get('count')}")
        x += 1


if __name__ == "__main__":
    log_stats()
