# -*- coding: utf-8 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

1. Keep the game going until the user types “exit”
1. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import os
clear = lambda: os.system("cls")
clear()

import random
x = random.randint(1, 9)

print("The computer has taken a random number. Try to guess the number!")

def Guess():
    number = int(input(": "))
    return number

number = Guess()
z = 0


