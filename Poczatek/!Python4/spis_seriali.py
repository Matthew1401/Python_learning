# -*- coding: utf-8 -*-
#Skrypt przechowywuje spis oglądanych seriali

serials={"Czarnobyl": 8.85, "Gra o tron": 8.76, "Breaking Bad": 8.76, "Nasza planeta": 8.67, "Kompania braci": 8.64}
choose=input("Jaki serial chciałbyś obejrzeć?\n")
print("Serial", choose, "ma ocenę", serials[choose])
new_serial=input("Jaki chciałbyś dodać nowy serial do listy?\n")
new_rating=input("I jakądał byś mu ocenę, w skali od 1 do 10?\n")
serials[new_serial]=new_rating
print(serials)