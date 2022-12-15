# -*- coding: utf-8 -*-
"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
import os
clear = lambda: os.system("cls")
clear()

a = 1
b = 0
c = 0


def Fibonnaci(a, b, c):
    repeat = int(input("How many fibonacci numbers would you like to generate?: "))
    for i in range(0, repeat):
        if i == 0:
            print("{}, ".format(a), end="")
            continue
        c = a + b
        if i == repeat-1:
            print(c)
        else:
            print("{}, ".format(c), end="")

        if a < b:
            a = c
        else:
            b = c

Fibonnaci(a, b, c)