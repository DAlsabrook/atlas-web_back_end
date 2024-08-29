#!/usr/bin/env python3
"""
Module that contains a function task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that does something with the called function and tracks
    its status

    Args:
        max_delay (int): max delay to use in base func

    Returns:
        asyncio.Task: task object used to track
    """
    return asyncio.create_task(wait_random(max_delay))
