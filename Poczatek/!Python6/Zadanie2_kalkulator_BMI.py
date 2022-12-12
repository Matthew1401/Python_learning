# -*- coding: utf-8 -*-
# Ćwiczenie na kalkulator BMI

weigh=float(input("Podaj swoją wagę[kg]:"))
height=float(input("Podaj swój wzrost[cm]: "))/100
BMI=weigh/height**2
print("BMI: {:.2f}".format(BMI))

if BMI < 18.5:
    print("Niedowaga")
elif 18.5 <= BMI < 24:
    print("Waga normalna")
elif 24 <= BMI < 26.5:
    print("Lekka nadwaga")
elif 26.5 <= BMI < 30:
    print("Nadwaga")
elif 30 <= BMI < 35:
    print("Otyłość I stopnia")
elif 35 <= BMI < 40:
    print("Otyłość II stopnia")
else:
    print("Otyłość III stopnia")