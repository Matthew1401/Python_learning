# -*- coding: utf-8 -*-
# Ćwiczenie na prostą grę

import os
clear = lambda: os.system("cls")
clear()

import random
x = random.randrange(0, 6)
lista = ["pączek", "domino", "bakłażan", "kalorie", "chrystus", "pomelo", "cudzysłów"]
slowo = lista[x]

word = ''.join(random.sample(slowo, len(slowo)))
print(word, "\n")


while x != slowo:
    x = input("Czy znasz rozwiązanie? Wpisz je :) (q lub Q by zakończyć)\n")
    if x == "q" or x == "Q":
        print("...")
        break
    elif x == slowo:
        print("\nGratki")
