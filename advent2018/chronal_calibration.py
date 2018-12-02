#!/usr/bin/env python

import sys
from itertools import accumulate


def calc_resulting_freq(in_array):
    return sum([int(x) for x in in_array])

def calc_repeat_freq(in_array):
    # Want to explicitly state we're starting at o
    num_array = [int(x) for x in in_array]
    mod_array = [0] + num_array
    cumulate_arr = accumulate(mod_array)

    # Legend for records dictionary object
    # Key = value, Value = index of previous observation
    records = {}
    repeat_freq = None
    for idx, val in enumerate(cumulate_arr):
        if val not in records.keys():
            records[val] = idx
        else:
            repeat_freq = records[val]
            break

    return repeat_freq


if __name__ == "__main__":
    data = sys.argv[1]  # Take file argument input
    with open(data, "r") as fh:
        raw = fh.read().splitlines()

    print("Result frequency:", str(calc_resulting_freq(raw)))
    print("Result repeat frequency:", str(calc_repeat_freq(raw)))
