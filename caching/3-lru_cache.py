#!/usr/bin/env python3
"""
Module that contains a class for LRU caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class to implement LRU caching
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lruItem = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(lruItem))
                del self.cache_data[lruItem]

    def get(self, key):
        """Get an item by key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
