#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value) seconds
and eventually returns it.
"""
from typing import List, Callable
wait_random: Callable = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function to generate a list of delays from a function that waits a
    random amount of time

    Args:
        n (int): How many times to call the function
        max_delay (int): max amount of time you want the function to wait

    Returns:
        List[float]: list of delays used
    """
    delay_list = [await wait_random(max_delay) for i in range(0, n)]
    return delay_list
