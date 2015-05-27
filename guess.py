#!/usr/local/bin/python3
"""Program guess a number"""

secretnum = 12
counter = 0 
while True:
    if counter >= 5:
        print("Sorry, the number was", secretnum)
        break
    guessnum = int(input("Guess a number: "))
    if guessnum > secretnum:
        print("Guess higher")
    elif guessnum < secretnum:
        print("Guess lower")
    else:
        print("Correct! Well done, the number was", secretnum)
        break
    counter += 1