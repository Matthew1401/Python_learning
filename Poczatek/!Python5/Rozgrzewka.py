# -*- coding: utf-8 -*-
#Proste ćwiczenie modyfikacji tekstów

sentence="Kurs Pythona jest prosty i przyjemny."
print("sentence = ", sentence)
print("Ilość znaków w zmiennej sentence: ", len(sentence))
print(sentence[18:-12]) # "prosty"
print(sentence[7]) # "t"
print(sentence[12]) # " "
print(sentence[-4]) # "m"
print(sentence[36]) # błąd
sentence=sentence[:2] + 'ś' + sentence[4:8] + 'ó' + sentence[10:]
print(sentence)