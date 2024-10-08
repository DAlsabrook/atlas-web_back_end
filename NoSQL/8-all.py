#!/usr/bin/end python3
""" Module for method to list documents
"""

def list_all(mongo_collection):
    """List all documents in collection
    """
    return mongo_collection.find()
