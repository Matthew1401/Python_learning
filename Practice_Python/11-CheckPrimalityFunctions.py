# -*- coding: utf-8 -*-
"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.)
"""
import os
clear = lambda: os.system("cls")
clear()

num = int(input("Give a number: "))
a = [i for i in range(2, num) if num % i == 0]


def is_prime(num):
    if num > 0:
        if len(a) == 0:
            print("Is prime!")
        else:
            print("Is NOT prime!")
    else:
        print("Is NOT prime!")

is_prime(num)