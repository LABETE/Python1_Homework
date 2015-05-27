#!/usr/local/bin/python3
"""Program that multipy numbers in a tuple."""

tuple_numbers = ((1,1), (2,2), (12,13), (4,4), (99,98))
for first_number, second_number in tuple_numbers:
    result = first_number * second_number
    print("{0:4d} = {1:2d} x {2:2d}".format(result, first_number, second_number))