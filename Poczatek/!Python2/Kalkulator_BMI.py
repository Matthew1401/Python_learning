# -*- coding: utf-8 -*-
#Kalkulator BMI, dla użytkownika

print("Obliczymy twoje BMI :)")
height=float(input("Podaj swój wzrost[cm]: "))/100
weight=float(input("Podaj swoją wagę[kg]: "))
print("Twoje BMI wynosi:",weight/height**2)