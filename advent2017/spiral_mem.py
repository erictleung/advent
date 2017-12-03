#!/usr/bin/env python

import sys
import csv


def odd_number_index(odd):
    """
    Return numbered odd number given after one

    Works only on positive numbers.

    :param odd: number to which to check which odd number it is
    :returns: integer of what odd number is given, -1 if even

    >>> odd_number_index(1)
    0

    >>> odd_number_index(3)
    1

    >>> odd_number_index(9)
    4

    >>> odd_number_index(10)
    -1
    """
    idx = -1

    # If number isn't even odd, don't bother with rest of function
    if (odd % 2) == 0:
        return idx

    # Brute force look up what number the odd number is
    for i in range(odd):
        odd_num = 2*i + 1
        if odd_num == odd:
            idx = i
            break

    return idx


def spiral_mem(number):
    return 0


if __name__ == "__main__":
    # Run script on command line
    # $ python advant2017/spiral_mem.py 347991

    # Take file argument input
    number = sys.argv[1]

    # Return calculated checksum
    spiral_mem(number)
