#!/usr/bin/env python3
"""Inserts a document in a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document based on kwargs and return the new _id."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
