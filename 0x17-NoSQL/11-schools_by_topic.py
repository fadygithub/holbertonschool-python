#!/usr/bin/env python3
"""search function"""


def schools_by_topic(mongo_collection, topic):
    """Return list of school with a specific topic"""
    return mongo_collection.find({"topics": topic})
