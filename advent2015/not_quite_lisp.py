#!/usr/bin/env python

import sys
from itertools import accumulate


def which_santas_floor(instructions):
    instruction_translation = map(left_or_right_val, instructions)
    return sum(instruction_translation)


def left_or_right_val(paren):
    if paren == "(":
        return 1
    else:
        return -1


def first_char_to_basement(instructions):
    instruction_translation = list(map(left_or_right_val, instructions))
    accumulate_sum = accumulate(instruction_translation)
    neg_one_indices = [idx for idx, x in enumerate(accumulate_sum) if x == -1]
    return neg_one_indices[0] + 1


if __name__ == "__main__":
    data = sys.argv[1]  # Take file argument input
    with open(data, "r") as fh:
        raw = fh.readline().rstrip()
    print("Final floor: ", str(which_santas_floor(raw)))
    print("First basement: ", str(first_char_to_basement(raw)))
