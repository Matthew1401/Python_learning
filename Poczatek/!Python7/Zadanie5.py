# -*- coding: utf-8 -*-
# Ćwiczenie na wyświetla nie choinki z trójkątów

import os
clear = lambda: os.system("cls")
clear()

x=int(input("Podaj ile razy ma wyświetlić się choinka:\n"))


for i in range(1, x+1):
    for j in range(1, i+2):
        print("#" * j)