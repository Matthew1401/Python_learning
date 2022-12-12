# -*- coding: utf-8 -*-
# Ćwiczenie na robienie pętli

import os
clear = lambda: os.system("cls")
clear()


x=int(input("Podaj ile razy ma powtórzyć się pętla:\n"))
print("x =", x)


if x % 3 == 0:
    w3=True
else:
    w3=False

if x % 4 == 0:
    w4=True
else:
    w4=False


for i in range(0, x):
    print("Czy liczba", x, "jest wielokrotnością liczby 3:", w3)
    print("Czy liczba", x, "jest wielokrotnością liczby 4:", w4)
    if w3 == True and w4 == True:
        print("Hurra!")
    elif w3 == False and w4 == False:
        print("*")
    print("")