#!/usr/bin/env python3
"""module that contains method for updating document
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Changes all topics of document based on name"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
