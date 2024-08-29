#!/usr/bin/env python3
"""
Module that contains an func that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n. Returns a float.
"""
import time, asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay:int) -> float:
    """Measures the time it takes to run wait_n function

    Args:
        n (int): amount of times wait_n runs a its callable
        max_delay (int): max delay for base function to wait

    Returns:
        float: roughly the time it takes to run 1 time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n

# n = 5
# max_delay = 9

# print(measure_time(n, max_delay))
