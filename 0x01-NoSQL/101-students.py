#!/usr/bin/env python3
"""
a script that gives students sorted by average score
"""


def top_students(mongo_collection):
    """
    a function that returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
