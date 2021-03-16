#!/usr/bin/env python3
"""Change the school topics"""


def update_topics(mongo_collection, name, topics):
    """Change topics of school document based on the name """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
