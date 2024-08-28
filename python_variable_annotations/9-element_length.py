#!/usr/bin/env python3
"""
Module to practice duck typing
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Retuns a list of tuples which contains a variable and its length

    Args:
        lst (Iterable[Sequence]): Some list with items in it

    Returns:
        List[Tuple[Sequence,int]]: A list of tuples that contain a variable
        and that variables length
    """
    return [(i, len(i)) for i in lst]
