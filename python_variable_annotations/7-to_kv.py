#!/usr/bin/env python3
"""
Module that contains a type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple. The first element of the
tuple is the string k. The second element is the square of the int/float v and
should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts passed str and float or int to a tuple

    Args:
        k (str): String to add as key
        v (Union[int, float]): Flaot or int to add as value

    Returns:
        tuple[str, float]: Combination to kv pair of passed in args
    """
    return (k, float(v ** 2))
