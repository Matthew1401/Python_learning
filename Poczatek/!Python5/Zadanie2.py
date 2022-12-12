# -*- coding: utf-8 -*-
#Proste ćwiczenie modyfikacji tekstów

#1
name=input("Podaj swoje imię: ")
surname=input("Podaj swoje nazwisko: ")
tel=input("Podaj nr telefonu: ")
print("name to tylko litery:", name.isalpha())
print("surname to tylko litery:", surname.isalpha())
print("tel to tylko cyfry:", tel.isdigit())

#2
name=name.capitalize()
surname=surname.capitalize()

#3
tel=tel.replace("-", "",).replace(" ", "")
print(tel)

#4
print("Czy podane imie jest żeńskie?", name.endswith("a"))

#5
personal=name + " " + surname + " " + tel
print(personal)

#6
print(len(personal))

#7
print(len(personal[:-10])-1)