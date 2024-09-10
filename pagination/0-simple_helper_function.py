#!/usr/bin/env python3
"""
Module for a function pagination set up
"""


def index_range(page, page_size):
    """function to get index of pagination range
    """
    max = page_size * page
    min = page_size * (page - 1) if page > 1 else 0
    return (min, max)
