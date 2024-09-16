#!/usr/bin/env python3
"""
This module contains the functions used to hide personal data
"""
import re
from typing import List
import logging


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
        userInfo = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        # print(userInfo)
        record.msg = userInfo
        # print(record.getMessage())
        return super(RedactingFormatter, self).format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    function to hide specific fields from a string with regex

    Returns a single string with fields hidden by what is passed to redaction.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, f"\\1={redaction}", message)

# message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
# log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
# formatter = RedactingFormatter(fields=("email", "ssn", "password"))
# print(formatter.format(log_record))
