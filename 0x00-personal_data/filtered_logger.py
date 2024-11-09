#!/usr/bin/env python3
"""
Filter logger module
"""
import re
from typing import List


def filter_datum(
        fields: List, redaction: str, message: str, separator: str
        ) -> str:
    """Returns the log message obfuscated"""
    patterns = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(patterns, lambda x: x.group(1) + '=' + redaction, message)
