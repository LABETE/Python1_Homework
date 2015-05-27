#!/usr/local/bin/python3

upperstring = input("Please enter an upper-case string ending with a period: ")
if upperstring.isupper() and upperstring.endswith("."):
    print("Input meets both requirements.")
elif not upperstring.isupper() and not upperstring.endswith("."):
    print("Input is not all upper case.")
    print("Input does not end with a period.")
elif not upperstring.isupper():
    print("Input is not all upper case.")
else:
    print("Input does not end with a period.")