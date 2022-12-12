# -*- coding: utf-8 -*-
# Ćwiczenie na obliczanie silni pętlą for

import os
clear = lambda: os.system("cls")
clear()

def silnia():
    s=1
    for i in range(1, n+1):
        s = s * i
    return s


n = int(input("Podaj dowolną liczbę całkowitą do 15: "))


if 0 < n <= 15:
    s = silnia()
    print(s)
else:
    print("Czy nie jasno wyraziłem polecenie?\nLiczbę całkowitą do 15\nOd 0 do 15 ;)")
