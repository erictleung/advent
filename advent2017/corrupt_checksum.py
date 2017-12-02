#!/usr/bin/env python

import sys
import csv


def two_d_arr_to_num(in_arr):
    return [[int(el) for el in arr] for arr in in_arr]


def calc_checksum(in_arr):
    int_arr = two_d_arr_to_num(in_arr)  # Make sure elements are integers
    return sum([int(max(arr)) - int(min(arr)) for arr in int_arr])


if __name__ == "__main__":
    # Take file argument input
    data = sys.argv[1]

    # Read in data from file
    raw = list(csv.reader(open(data, "r"), delimiter="\t"))

    # Return calculated checksum
    print(calc_checksum(raw))
