#!/usr/bin/env python3
"""
Module to handle a redis cache
"""
import uuid
import redis
from typing import Union, Callable


class Cache():

    def __init__(self):
        """initialize"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data"""
        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self, key: str, fn: Callable):
        """Run a cache object through a function if exists"""
        cacheValue = self._redis.get(key)
        if (not cacheValue):
            return cacheValue
        return fn(cacheValue)

    def get_str(self, key: str) -> Union[str, None]:
        """Get a string value from the cache"""
        return self.get(key, lambda x: str(x))

    def get_int(self, key: str) -> Union[int, None]:
        """Get an integer value from the cache"""
        return self.get(key, lambda x: int(x))
