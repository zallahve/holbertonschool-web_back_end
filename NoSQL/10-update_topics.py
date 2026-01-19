#!/usr/bin/env python3
"""Updates topics of school documents in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """Update all documents with given name, setting their topics list."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
