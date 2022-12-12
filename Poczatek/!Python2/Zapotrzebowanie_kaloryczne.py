# -*- coding: utf-8 -*-
#Obliczanie zapotrzebowania kalorycznego dla mężczyzny
#https://www.flynerd.pl/2017/01/python-1-zabawy-w-konsoli.html


height=int(input("Witaj mężczyzno!\nObliczymy twoje zapotrzebowanie kaloryczne :)\nPodaj swój wzrost[cm]:\n"))
weight=int(input("Podaj swoją wagę[kg]:\n"))
age=int(input("Podaj swój wiek:\n"))
s=5
print("Twoje zapotrzebowanie kaloryczne to", 10*weight +6.25*height -5*age +s, "kcal")
