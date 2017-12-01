#!/usr/bin/env python

import sys


def inv_captcha(in_num):
    # Take number and split up digits into list
    digits = [int(i) for i in str(in_num)]
    final_sum = 0

    # Loop through all digits
    digit_list_idx = range(len(digits))
    for i in digit_list_idx:
        # Get current digit
        curr_digit = digits[i]

        # Check if looking at last digit
        if i == len(digits) - 1:
            if digits[0] == digits[i]:
                final_sum += digits[i]
        else:
            # Check if digit matches next digit in list
            if digits[i] == digits[i + 1]:
                final_sum += digits[i]

    return final_sum

def half_captcha(in_num):
    final_sum = 0
    return final_sum


if __name__ == "__main__":
    data = sys.argv[1] # Take file argument input
    with open(data, "r") as fh:
        raw = fh.readline().rstrip()
    print(inv_captcha(raw))
