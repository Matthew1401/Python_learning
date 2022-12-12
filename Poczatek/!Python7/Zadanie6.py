# -*- coding: utf-8 -*-
# Ćwiczenie na wyświetla tabliczki mnożenia

import os
clear = lambda: os.system("cls")
clear()

szer=56
print("-" * szer)
print("|    |", end="")
for i in range(1, 11):
    print(" {:3d}|". format(i), end="")
print()


for i in range(1, 11):
    print("| {:3d}|".format(i), end="")
    for j in range(1, 11):
        print(" {:3d}|".format(j*i), end="")
    print()
print("-" * szer)