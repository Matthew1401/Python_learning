# -*- coding: utf-8 -*-
# Ćwiczenie z twierdzeniem pitagorasa

import os
clear=lambda: os.system('cls')
clear()


print("Sprawdzamy boki różne właściwości boków trójkąta")
a=int(input("Podaj bok a: "))
b=int(input("Podaj bok b: "))
c=int(input("Podaj bok c: "))


if b < a > c:
    max=a
    if b < c:
        med=c
        min=b
    else:
        med=b
        min=c
elif a < b > c:
    max=b
    if a < c:
        med=c
        min=a
    else:
        med=a
        min=c
else:
    max=c
    if a < b:
        med=b
        min=a
    else:
        med=a
        min=b

c=max
b=med
a=min


def t_egipt():
    if a/3 == b/4 == c/5:
        return "Trójkąt jest trójkątem egipskim"
    else:
        return "Trójkąt nie jest trójkątem egipskim"


def t_pitagoras():
    if c**2 == a**2 + b**2:
        return "Trójkąt jest trójkątem pitagorejskim!"
    else:
        return "Trójkąt nie jest trójkątem pitagorejskim"


if a + b <= c:
    print("Nie jest możliwe utworzenie trójkąta o podanych bokach :)")
else:
    print(t_pitagoras())
    print(t_egipt())