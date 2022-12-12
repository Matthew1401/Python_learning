# -*- coding: utf-8 -*-
# Ćwiczenie na zgadywanie liczb

import os
clear = lambda: os.system("cls")
clear()

import random
x = random.randrange(1, 30)


print("Komputer wylosował liczbę od 1 do 30, spróbój zgadnąć!")

y=0
while y != x:
    y=int(input())
print("Zgadłeś :)")