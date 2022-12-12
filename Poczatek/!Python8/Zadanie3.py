# -*- coding: utf-8 -*-
# Ćwiczenie na rozdzielanie imion w tekście

import os
clear = lambda: os.system("cls")
clear()


import random
x = random.randrange(1, 30)


print("Komputer wylosował liczbę od 1 do 30, spróbój zgadnąć!")

y=0
while y != x:
    y=int(input())
    if y < x:
        print("Podaj większą liczbę")
    elif y == x:
        break
    else:
        print("Podaj mniejszą liczbę")
print("Zgadłeś :)")