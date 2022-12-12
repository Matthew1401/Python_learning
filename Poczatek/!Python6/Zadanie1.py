# -*- coding: utf-8 -*-
# Ćwiczenie na sprawdzenie pełnoletności użytkownika

print("Ile masz lat?")
age = int(input())

if age > 100:
    print("200 lat ♫")
elif age >= 18:
    print("Użytkownik pełnoletni")
else:
    print("Użytkownik niepełnoletni")
    print("Do pełnoletności zostało", 18-age, "lat")