#!/usr/bin/env python3
"""
Module that contains a calss for caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class to interact with a cache

    Inherits:
        BaseCaching (_type_): Base class to inherit
    """

    def init(self):
        """initiliaze class
        """
        super().init()

    def put(self, key, item):
        """Add key, value to cache object
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache
        """
        return self.cache_data.get(key)
