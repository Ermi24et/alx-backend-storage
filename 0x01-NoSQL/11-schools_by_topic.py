#!/usr/bin/env python3
"""
where can i learn python
"""


def schools_by_topic(mongo_collection, topic):
    """
    a function that returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
