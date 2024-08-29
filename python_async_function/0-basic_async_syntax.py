#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value) seconds
and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """Waits a random amount of time and returns the delay

    Args:
        max_delay (int, optional): Max amount of time to wait. Defaults to 10.

    Returns:
        int: 
    """
    delay = random(0, max_delay)
    await asyncio.sleep(delay)
    return delay
