# -*- coding: utf-8 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import os
clear = lambda: os.system("cls")
clear()

import random
x = random.randint(1, 9)
z = 0 #Extras2 tracking how many guesses the user has taken


def Guess():
    number = (input(": "))
    if number.lower() == "exit":
        number = 0
        return number
    elif number == "0":
        number = 10
        return number
    else:
        return int(number)



print("The computer has taken a random number from 1 to 9. Try to guess the number!\nIf you want to quit TYPE: exit")


while True:
    z+=1
    number = Guess()
    if 0 < number < 10:
        if number == x:
            if z == 1:
                print("You won!\nYou took {} track to find it".format(z))
                break
            print("You won!\nYou took {} tracks to find it".format(z))
            break
        elif number < x:
            print("Look higher!")
        else:
            print("Look lower!")
    elif number == "exit":
        print("See you later!")
        break
    else:
        print("Enter the number from 1 to 9!")
        continue