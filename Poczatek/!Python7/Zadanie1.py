# -*- coding: utf-8 -*-
# Ćwiczenie na sumowanie poprzednich liczb

import os
clear = lambda: os.system("cls")
clear()


j=0

for i in range(1, 11):
    print(j+i)
    j=i+j