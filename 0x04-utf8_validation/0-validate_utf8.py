#!/usr/bin/python3
"""UTF8 validation
"""

def validUTF8(data):
    """Validates UTF8 strings bytewise
       Args: data
       Return: True if valid, False otherwise
    """
    # Number of bytes in the current character
    num_bytes = 0

    # Iterate through each byte in the data set
    for byte in data:
        # If this is the start of a new character
        if num_bytes == 0:
            # Determine the number of bytes in this character based on the first few bits
            if byte >> 7 == 0b0:
                num_bytes = 1
            elif byte >> 5 == 0b110:
                num_bytes = 2
            elif byte >> 4 == 0b1110:
                num_bytes = 3
            elif byte >> 3 == 0b11110:
                num_bytes = 4
            else:
                # Invalid start of a character
                return False
        else:
            # This byte should be part of the current character
            if byte >> 6 != 0b10:
                # Invalid continuation byte
                return False
            num_bytes -= 1

    # If we reached the end of the data set but there's still a character being parsed
    if num_bytes > 0:
        return False

    return True
