#!/usr/bin/env python

import sys


def which_santas_floor(instructions):
    instruction_translation = map(left_or_right_val, instructions)
    return sum(instruction_translation)


def left_or_right_val(paren):
    if paren == "(":
        return 1
    else:
        return -1


if __name__ == "__main__":
    data = sys.argv[1]  # Take file argument input
    with open(data, "r") as fh:
        raw = fh.readline().rstrip()
    print(which_santas_floor(raw))
