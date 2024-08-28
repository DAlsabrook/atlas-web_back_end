#!/usr/bin/env python3
"""
Module that contains a type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function to get the sum of a list

    Args:
        mxd_lst (List[int, float]): List to sum

    Returns:
        float: sum of list
    """
    return float(sum(mxd_lst))
