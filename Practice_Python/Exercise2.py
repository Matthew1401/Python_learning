# -*- coding: utf-8 -*-
"""

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
import os
clear = lambda: os.system("cls")
clear()

import time
year = time.gmtime()[0] #2022


name = input("Give me your name: ")
age = int(input("Enter your age: "))

if  0 < age < 100:
    birth = year - age + 100
    z = int(input("Give me another number: "))
    print("You will be 100 years old in {}.\n".format(birth) * z)
else:
    print("Is it your true age? Kid")