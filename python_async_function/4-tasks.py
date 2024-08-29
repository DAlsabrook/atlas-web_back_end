#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value) seconds
and eventually returns it.
"""
from typing import List, Union
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function to generate a list of delays from a function that waits a
    random amount of time

    Args:
        n (int): How many times to call the function
        max_delay (int): max amount of time you want the function to wait

    Returns:
        List[float]: list of delays used
    """
    delay_list = [await task_wait_random(max_delay) for i in range(0, n)]
    bubble(delay_list)
    return delay_list


def bubble(list: List[Union[int, float]]):
    """Function to organize a list in ascending order

    Args:
        list (List[Union[int, float]]): List to sort
    """
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
