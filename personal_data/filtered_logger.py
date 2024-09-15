#!/usr/bin/env python3
"""
This module contains the functions used to
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    function to hide specific fields from a string with regex
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, f"\\1={redaction}", message)
