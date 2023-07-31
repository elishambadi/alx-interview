#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    valiUTF8 - checks if UTF8 data is valid
    """

    num_bytes_to_check = 0

    for num in data:
        if num_bytes_to_check == 0:
            if num & 0b10000000 == 0:
                num_bytes_to_check = 0
            elif num & 0b11100000 == 0b11000000:
                num_bytes_to_check = 1
            elif num & 0b11110000 == 0b11100000:
                num_bytes_to_check = 2
            elif num & 0b11111000 == 0b11110000:
                num_bytes_to_check = 3
            else:
                return False
        else:
            if num & 0b11000000 != 0b10000000:
                return False
            num_bytes_to_check -= 1
    return num_bytes_to_check == 0
