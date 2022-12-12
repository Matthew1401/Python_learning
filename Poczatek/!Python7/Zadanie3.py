# -*- coding: utf-8 -*-
# Ćwiczenie na rozdzielanie imion w tekście

import os
clear = lambda: os.system("cls")
clear()

print("Wpisz różne imiona!\nImiona oddziel ',' albo spacją' ")
names=input()
names=names.title()
names=names[::] + " "


if names.count(", ") > 0:
    names=names.replace(",", "")
elif names.count(",") > 0:
    names=names.replace(",", " ")


if names.count(",") == 0:
    numbers_names=names.count(" ")
    for i in range(0, numbers_names):
        numbers_name=names.find(" ")
        print("Hi, you are cute", names[:numbers_name], "!")
        names="" + names[numbers_name+1:]

