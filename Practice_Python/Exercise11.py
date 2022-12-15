# -*- coding: utf-8 -*-
"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.)
"""
import os
clear = lambda: os.system("cls")
clear()

a=[]

def get_number(help_text="Give a number: "):
    return int(input(help_text))

num = get_number()
i = num


while i != 0:
    if num % i == 0:
        a.append(i)
    i-=1

if len(a) == 2:
    print("Your number is prime")
else:
    print("Your number is not prime")