#!/usr/bin/env python3
""" Module for method to list documents
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in collection
    """
    return mongo_collection.find()
