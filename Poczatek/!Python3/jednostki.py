# -*- coding: utf-8 -*-
#Skrypt konwertuje jednostki z cm na metry i cale oraz z kd na funty

cm=float(input("Podaj liczbę w cm:\n"))
m=cm/100
cal=cm/2.54
print("Metry: {:.2f}\nCale: {:.2f}".format(m, cal))

kg=float(input("Podaj liczbę w kg:\n"))
funty=kg*2.20462262
print("Funtów jest: {:.3f}".format(funty))