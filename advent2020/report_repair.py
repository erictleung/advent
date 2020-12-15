#!/usr/bin/env python3

def multiply_twenty_twenty(in_list):

    new_list = [2020 - x for x in in_list]
    good_nums = list(set(start_list) & set(new_list))

    return(good_nums[0] * good_nums[1])


if __name__ == "__main__":
    data = sys.argv[1]  # Take file argument input
    with open(data, "r") as fh:
        raw = fh.read().splitlines()
