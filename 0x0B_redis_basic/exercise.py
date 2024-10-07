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


def call_history(method: Callable) -> Callable:
    """Everytime the original function is called, add its input parameters
    to one list in redis, and store its output into another list"""
    @wraps(method)
    def methodHugger(self, *args, **kwargs):
        inputsKey = f"{method.__qualname__}:inputs"
        self._redis.rpush(inputsKey, str(args))

        result = method(self, *args, **kwargs)

        outputsKey = f"{method.__qualname__}:outputs"
        self._redis.rpush(outputsKey, str(result))
        return result
    return methodHugger


class Cache():

    def __init__(self):
        """initialize"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    @call_history
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


def replay(method: Callable) -> str:
    """function to display the history of calls of a particular function"""
    redis = method.__self__._redis
    method_name = method.__qualname__

    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    inputs = redis.lrange(inputs_key, 0, -1)
    # Start at first element 0 and end at last element in list -1
    outputs = redis.lrange(outputs_key, 0, -1)
    # Grab method call count
    call_count = redis.get(method_name).decode('utf-8')

    print(f"{method_name} was called {call_count} times:")
    for input, output in zip(inputs, outputs):
        print(f"{method_name}(*{input.decode('utf-8')}) -> {output.decode('utf-8')}")
