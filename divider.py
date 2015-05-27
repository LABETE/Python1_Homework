#!/usr/local/bin/python3
""" Program get the result of 10 / an integer """

print("Dividing 10 by an integer")
while True:
    usr_inp = input("Provide an integer: ")
    if not usr_inp:
        break
    try:
        result = 10/int(usr_inp)
        print("The result of 10 / {0} is: {1}".format(usr_inp,result))
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")