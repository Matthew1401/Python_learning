# -*- coding: utf-8 -*-
# Ćwiczenie na wyświetlanie sześcianu liczb 1-10

import os
clear = lambda: os.system("cls")
clear()


for i in range(1, 11):
    print(i,"**3 =", i**3)