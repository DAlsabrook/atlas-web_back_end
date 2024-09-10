#!/usr/bin/python3
"""FIFO caching class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class to implement FIFO ording from the cache
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put an item in the object
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                firstIn = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(firstIn))
                del self.cache_data[firstIn]
            self.cache_data[key] = item

    def get(self, key):
        """Get a value from the dict or return None if doesnt exist
        """
        return self.cache_data.get(key)
