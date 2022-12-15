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

a = [5, 10, 15, 20, 25]

def lists_end():
    return [a[0], a[-1]]

new_list = lists_end()
print(new_list)