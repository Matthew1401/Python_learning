# -*- coding: utf-8 -*-
"""

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""

import os
clear = lambda: os.system("cls")
clear()


a =[]
num = int(input("Enter a number: "))
i = num

while i != 0:
    if num % i == 0:
        a.append(i)
    i-=1
print(a)