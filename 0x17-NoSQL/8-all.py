#!/usr/bin/env python3
""" List documents in Python """
import pymongo


def list_all(mongo_collection):
    """ list documents in the collection """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
