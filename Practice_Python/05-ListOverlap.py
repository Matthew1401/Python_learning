# -*- coding: utf-8 -*-
"""

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""

import os
clear = lambda: os.system("cls")
clear()

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for num in a:
    if num in b:
        c.append(num)
        b.remove(num)
print(c)


#Extras1
a = []
b = []
c = []
i = 2


while i != 0:
    j = random.randrange(1, 35)
    while j != 0:
        if i == 2:
            a.append(random.randrange(1, 99))
            j-=1
        elif i == 1:
            b.append(random.randrange(1, 99))
            j-=1
    i-=1


for num in a:
    if num in b:
        c.append(num)
        b.remove(num)
print(c)


#Extras2
print({1, 6, 5, 3, 7, 2, 2}.intersection([1, 6, 9, 34, 2, 2, 18, 790]))
print(set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]).intersection(set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))) 
