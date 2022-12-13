# -*- coding: utf-8 -*-
"""

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

import os
clear = lambda: os.system("cls")
clear()


text = input("I will check if your word is a palindrome or not.\nEnter a single word: ")
text1 = ""
#text1 = text[::-1]# we can use this instead loop 'for'
#print(text1)

for i in text:
    text1 = i + text1[:]

if text == text1:
    print("Word '{}' is a palindrome!".format(text))
else:
    print("Word '{}' is not a palindrome!".format(text))