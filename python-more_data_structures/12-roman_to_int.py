#!/usr/bin/python3


def roman_to_int(roman_string):
    res = 0
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}

    if roman_string is not str(roman_string) or roman_string is None:
        return 0

    for i in range(len(roman_string)):
        num1 = roman_numbers[roman_string[i]]
        if i < len(roman_string) - 1:
            if num1 < roman_numbers[roman_string[i + 1]]:
                num1 = 0 - num1
        res += num1

    return res
