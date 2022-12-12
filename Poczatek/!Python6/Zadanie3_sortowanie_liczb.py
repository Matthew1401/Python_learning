# -*- coding: utf-8 -*-
# Ćwiczenie na sortowanie liczb

import os
clear=lambda: os.system('cls')
clear()
import random
a=random.randint(1000, 999999)
b=random.randint(1000, 999999)
c=random.randint(1000, 999999)

if b < a > c:
    max=a
    if b < c:
        med=c
        min=b
    else:
        med=b
        min=c
elif a < b > c:
    max=b
    if a < c:
        med=c
        min=a
    else:
        med=a
        min=c
else:
    max=c
    if a < b:
        med=b
        min=a
    else:
        med=a
        min=b
print("Kolejność losowych liczb to:")
print(min)
print(med)
print(max)
