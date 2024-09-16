#!/usr/bin/env python3
"""
This module contains the functions used to hide personal data
"""
import re
from typing import List
import logging
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Class initialization
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """This method formats the record.msg to be obfuscated
        """
        # should print format with correct info
        userInfo = filter_datum(self.fields, self.REDACTION,
                                record.getMessage(), self.SEPARATOR)
        # print(userInfo)
        record.msg = userInfo
        # print(record.getMessage())
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """The method creates a custom logger
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    function to hide specific fields from a string with regex

    Returns a single string with fields hidden by what is passed to redaction.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, f"\\1={redaction}", message)
