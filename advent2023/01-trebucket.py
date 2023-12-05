#!/usr/bin/env python3

import re
from pprint import pprint

# Part 1

with open("../data/2023_day1.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]

# Strip first and last numbers
number_pairs_strs = [(
    re.search(r"\d", x[::]).group(),
    re.search(r"\d", x[::-1]).group())
    for x in content
]

# Combine first and last number per string into single number
all_numbers = [int(x[0] + x[1]) for x in number_pairs_strs]

# Add all numbers
total = sum(all_numbers)
print(f"Part 1: {total}")

# Part 2

num_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}
# Overlapping strings
# https://stackoverflow.com/q/20833295
re_nums = "(?=(" + "|".join(list(num_words.keys())) + "))"
# print(re_nums)

# For testing
# with open("../data/2023_day1_pt2.txt") as f:
#     content = f.readlines()
#     content = [x.strip() for x in content]
test = 100

nums = [re.findall(re_nums, x) for x in content]
# print(nums[:test], "\n")

# Edge cases when there is just one value
parsed_nums = [x + ["0"] if len(x) == 1 else x for x in nums]
# print(parsed_nums[:test], "\n")

# Strip first and last numbers
number_pairs_strs = [(x[0], x[-1]) for x in parsed_nums]
# print(number_pairs_strs[:test], "\n")

# Combine first and last number per string into single number
num_words["0"] = ""  # Add in element for search
all_numbers = [
    int(str(num_words[x[0]]) + str(num_words[x[1]]))
    for x in number_pairs_strs
]
# print(all_numbers[:test], "\n")

pprint(list(zip(nums, parsed_nums, number_pairs_strs, all_numbers))[:140])

# Add all numbers
total = sum(all_numbers)
print(f"Part 2: {total}")

# Tries
# 53032
# 50125
