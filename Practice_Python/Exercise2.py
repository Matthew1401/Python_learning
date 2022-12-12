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

number = int(input("Give me number: "))


if number % 4 == 0:
    print("Number {} is a multiple of 4".format(number))
elif number % 2 == 0:
    print("Number {} is even".format(number))
else:
    print("Number {} is odd".format(number))