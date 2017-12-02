#!/usr/bin/env python

import sys
import csv


def two_d_arr_to_num(in_arr):
    return [[int(el) for el in arr] for arr in in_arr]


def calc_checksum(in_arr):
    int_arr = two_d_arr_to_num(in_arr)  # Make sure elements are integers
    return sum([int(max(arr)) - int(min(arr)) for arr in int_arr])


def calc_even_checksum(in_arr):
    int_arr = two_d_arr_to_num(in_arr)  # Make sure elements are integers
    final_sum = 0
    for inner_arr in int_arr:
        inner_arr.sort()  # Heuristic sort to lessen number of comparisons
        for idx, val in enumerate(inner_arr):
            # Divide inner array by an element in array
            div_array = list(map(lambda x: x % val, inner_arr))

            # Keep indices where remainder from division equal to zero
            idx_array = [idx for idx, val in enumerate(div_array) if val == 0]

            # Check if there were two numers that were evenly divisible
            if len(idx_array) == 2:
                # Access good numbers by indices we've deemed good
                good_nums = [inner_arr[i] for i in idx_array]
                break  # Leave for loop, we have numbers we want

        # There's only two numbers so just looking at maxes and mins is okay
        final_sum += max(good_nums) / min(good_nums)

    return final_sum


if __name__ == "__main__":
    # Take file argument input
    data = sys.argv[1]

    # Read in data from file
    raw = list(csv.reader(open(data, "r"), delimiter="\t"))

    # Return calculated checksum
    print("Checksum:", calc_checksum(raw))
    print("Even Checksum:", calc_even_checksum(raw))
