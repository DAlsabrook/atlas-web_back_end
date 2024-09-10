#!/usr/bin/env python3
"""
Module for a function pagination set up
"""


def index_range(page, page_size):
    """function to get index of pagination range
    """
    return (page_size * (page - 1) if page > 1 else 0, page_size * page)
