#!/usr/bin/env python3
"""module that contains method for inserting to collection
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
