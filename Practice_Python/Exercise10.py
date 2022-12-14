# -*- coding: utf-8 -*-
"""
This week’s exercise is going to be revisiting an old exercise,
except require the solution in a different way.

Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extra:
1. Randomly generate two lists to test this
"""
import os
clear = lambda: os.system("cls")
clear()

import random

a = random.sample(range(26), random.randint(1, 25))
b = random.sample(range(26), random.randint(1, 24))
ab = [element for element in a if element in b]
print(a)
print(b)
print(ab)