#!/usr/bin/env python3
"""
change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    a function that changes all topics of a school document based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})