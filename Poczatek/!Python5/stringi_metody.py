# -*- coding: utf-8 -*-
# Skrypt, który zawiera metody strongów

txt=" * Witam szanowne Państwo!1\n"

# Metody zwracające nowy napis (string):
print(txt.lower()) # Zmienia znaki na małe
print(txt.upper()) # Zmienia znaki na duże
print(txt.swapcase()) # Odwraca wielkość znaków
print(txt.capitalize()) # Zmienia pierwszą literę na dużą
print(txt.title()) # Zamienia 1 literę każdego wyrazu na dużą
print(txt.join("Jezus ")) # Ten napis w join() jest od góry od dołu
print(txt.lstrip()) # Usuwa białe znaki z lewej strony, czyli spacje, tabulatory
print(txt.rstrip()) # To samo z prawej
print(txt.strip(" *")) # Usuwa białe znaki, lub znak podany w () z początku i końca
print(max(txt)) # Zwraca litere najdalej w alfabecie od A
print(min(txt)) # Zwraca literę najbliżej w alfabecie A, tylko w konsoli nic mi sięnie wyświetla :(
print(txt.split(" ")) # Dzieli tekst według podanego znaku
print(txt.replace("szanowne", "ułomne")) # Podmienia podane znaki

# Metody zwracające wartość liczbową:
print(len(txt)) # Zwraca długość ciągu znaków
print(txt.count("a")) # Liczy ilość podanych znaków
print(txt.find("e ")) # Liczy ilość znaków do podanego znaku
print(txt.rfind("e ")) # Podobno ma działać tak jak find(), ale liczyć od końca, ale wynik wychodzi mi identyczny

# Metody zwracające true/false
print(txt.isalnum()) # True - jeśli wszystkie znaki to litery lub cyfry
print(txt.isalpha()) # True - jeśli wszystkie znaki to litery
print(txt.isdigit()) # True - jeśli wszystkie znaki to cyfry
print(txt.islower()) # True - jeśli wszystkie znaki to małe litery
print(txt.isupper()) # True - jeśli wszystkie znaki to duże litery
print(txt.isspace()) # True - jeśli wszystkie znaki to białe znaki
print(txt.istitle()) # True - jeśli wszystkie wyrazy zaczynają się z dużych liter
print(txt.startswith(" * ")) # True - jeśli początek tekstu zgadza się z tym w ()
print(txt.endswith("!1\n")) # True - jeśli koniec tekstu zgadza się z tym podanym w ()
