# -*- coding: utf-8 -*-
# Ćwiczenie na sortowanie liczb

import os
clear=lambda: os.system('cls')
clear()

def again():
    gen=input("Wpisz czy Twoje imie jest męskie[m], czy żeńskie[ż]:")
    if gen == 1:
        names[name]=gen
    elif gen == 0:
        names[name]=gen
    else:
        again()

names={
    "Oskar": "meskie",
    "Mateusz": "meskie",
    "Weronika": "zenskie",
    "Justyna": "zenskie"}

name=input("Podaj swoje imię: ")
name=name.capitalize()

if name in list(names.keys()):
    print(name, "to imię", names[name])
else:
    print("Nie mamy takiego imienia. Dodaj je do zbioru!")
    gender = input("To imię żeńskie czy męskie? Wpisz m/z: ")
    if gender == "m":
        names[name]="meskie"
    elif gender == "z":
        names[name]="zenskie"
    else:
        print("Musisz podać jaki to rodzaj imienia!")

print (list(names.keys()))
    