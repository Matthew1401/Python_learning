# -*- coding: utf-8 -*-
"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Note: for this exercise, the expectation is that you explicitly write out the year
(and therefore be out of date the next year).

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines.
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