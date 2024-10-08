#!/usr/bin/python3
"""LIFO caching class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class to implement LIFO ording from the cache
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put an item in the object
        """
        if key and item:
            cacheLength = len(self.cache_data)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # print(cacheLength, BaseCaching.MAX_ITEMS)
                lastIn = list(self.cache_data.keys())[cacheLength - 1]
                print('DISCARD: {}'.format(lastIn))
                del self.cache_data[lastIn]

    def get(self, key):
        """Get a value from the dict or return None if doesnt exist
        """
        return self.cache_data.get(key)
