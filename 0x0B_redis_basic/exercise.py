#!/usr/bin/env python3
"""
Module to handle a redis cache
"""
import uuid
import redis
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a method using Redis"""
    @wraps(method)
    def methodHugger(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key) #increment value at key
        result = method(self, *args, **kwargs)
        return result
    return methodHugger


class Cache():

    def __init__(self):
        """initialize"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data"""
        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self, key: str, fn: Callable = None):
        """Run a cache object through a function if exists"""
        cacheValue = self._redis.get(key)
        if cacheValue is None:
            return None
        if fn is None:
            return cacheValue
        return fn(cacheValue)

    def get_str(self, key: str) -> Union[str, None]:
        """Get a string value from the cache"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """Get an integer value from the cache"""
        try:
            return self.get(key, lambda x: int(x))
        except ValueError:
            raise ValueError()
