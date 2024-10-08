#!/usr/bin/env python3
"""
Module that contains a function sum_list which takes a list input_list of
floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function to get the sum of floats in a list

    Args:
        input_list (list[float]): List of floats passed in

    Returns:
        float: Sum of floats
    """
    return sum(input_list)
