#!/usr/bin/python3
"""
a simple module to test the encodeing of the
data recieved to function validUTF8
"""


def validUTF8(data):
    """
    valdiating number of bits for data
    whether it's number or char or Bool
    """
    for item in data:
        try:
            bit_length = item.bit_length()
            if bit_length > 8:
                return False
        except AttributeError:
            return item.isascii()
    return True
