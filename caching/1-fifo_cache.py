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
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                firstIn = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(firstIn))
                del self.cache_data[firstIn]


    def get(self, key):
        """Get a value from the dict or return None if doesnt exist
        """
        return self.cache_data.get(key)

if __name__ == '__main__':
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
