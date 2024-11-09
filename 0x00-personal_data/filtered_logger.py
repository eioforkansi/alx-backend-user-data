#!/usr/bin/env python3
"""
Filter logger module
"""
import re
from typing import List
import logging


# Define PII fields as a tuple
PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(
        fields: List, redaction: str, message: str, separator: str
        ) -> str:
    """Returns the log message obfuscated"""
    pattern = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(pattern, lambda x: x.group(1) + '=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class to redact sensitive fields in log records."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize with list of fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redact specified fields in the log message."""
        msg = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)

def get_logger() -> logging.Logger:
    """To set up the logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Set up StreamHandler with RedactingFormatter
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger