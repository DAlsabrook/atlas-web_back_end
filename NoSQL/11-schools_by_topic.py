#!/usr/bin/env python3
"""module that contains method for listing specific topic
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """Get schools by topic"""
    return list(mongo_collection.find({ "topics": topic }))
