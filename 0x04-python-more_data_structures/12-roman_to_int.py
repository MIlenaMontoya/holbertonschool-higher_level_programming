#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    res = 0
    num = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for n in reversed(roman_string):
        num = rom[n]
        res += num if res < num * 5 else -num
    return res
