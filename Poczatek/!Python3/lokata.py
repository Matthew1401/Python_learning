# -*- coding: utf-8 -*-
#Skrypt oblicza stan konta (lokaty)

k0=float(input("Podaj początkowy stan konta [zł]:\n"))
n=int(input("Podaj ile lat ma trwać lokata:\n"))
m=12
r=int(input("Podaj stopę oprocentowania rocznego [%]:\n"))
wynik=k0*(1+r/m)**(m*(n/100))
print("{:.2f}zł przez {} lata na lokacie {}% urośnie do {:.2f}".format(k0, n, r, wynik))