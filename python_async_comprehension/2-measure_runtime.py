#!/usr/bin/env python3
"""
Module that calls an async generator and measures the time it takes to run
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function to measure run time of async generator

    Returns:
        float: Amount of time that it took to run
    """
    startTime = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    endTime = time.time()
    return endTime - startTime

# print(asyncio.run(measure_runtime()))
