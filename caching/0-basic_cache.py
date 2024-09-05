#!/usr/bin/env python3
BaseCaching = __import__('./base_caching.py').BaseCaching

class BasicCache(BaseCaching):

    def init(self):
        super().init()

    def put(self, key, item):
        print('hi')

    def get(self, key):
        print('hello')
