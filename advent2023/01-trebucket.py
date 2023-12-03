#!/usr/bin/env python3

import re

with open("../data/2023_day1.txt") as f:
    content = f.readlines()

# Extract everything into a list
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
print(total)
