#!/usr/bin/env python3
"""
Module that contains a class for MRU caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Class to implement MRU caching
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
                mruItm = list(self.cache_data.keys())[len(self.cache_data) - 2]
                print('DISCARD: {}'.format(mruItm))
                del self.cache_data[mruItm]

    def get(self, key):
        """Get an item by key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
