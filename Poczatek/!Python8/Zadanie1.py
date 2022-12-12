# -*- coding: utf-8 -*-
# Ćwiczenie na pętle while

import os
clear = lambda: os.system("cls")
clear()

num1=1
num2=0

while num1 <= 10:
    num2 += num1
    print("{},".format(num2), end=" ")
    num1 += 1