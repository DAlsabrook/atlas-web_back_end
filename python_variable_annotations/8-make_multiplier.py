#!/usr/bin/env python3
"""
Module that contains a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies a float
by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function with a multiplier

    Args:
        multiplier (float): Arg to use as multiplier

    Returns:
        Callable[[float], float]: function to return to caller
    """
    def multiplierFunc(num: float) -> float:
        return num * multiplier
    return multiplierFunc

