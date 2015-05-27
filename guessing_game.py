#!/usr/local/bin/python3
"""Program for guess a random number"""

import random

random_number = random.randint(1, 99)
while True:
    guess_number = int(input("Guess a number between 1 and 99: "))
    if guess_number > random_number:
        print("Too high")
    elif guess_number < random_number:
        print("Too low")
    else:
        print("You guessed it!, Congratulations!")
        break