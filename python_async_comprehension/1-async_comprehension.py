#!/usr/bin/env python3
"""
Module that calls an async generator
"""
# import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine that get 10 numbers from an async generator
    in an async for
    """
    return [randNumber async for randNumber in async_generator()]

# print(asyncio.run(async_comprehension()))
