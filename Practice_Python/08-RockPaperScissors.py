# -*- coding: utf-8 -*-
"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:
* Rock beats scissors
* Scissors beats paper
* Paper beats rock
"""

import os
clear = lambda: os.system("cls")
clear()

print("Welcome in the Rock-Paper-Scissors game!")
print("If you want to have fun, you should be with other person")

def Choose1():
   player1 = input("Choose (Player1):\n1. Rock\n2. Paper\n3. Scissors\n: ")
   return player1

def Choose2():
    player2 = input("Choose (Player2):\n1. Rock\n2. Paper\n3. Scissors\n: ")
    return player2

def Win1():
    print("Congratulations Player1 YOU WON!")

def Win2():
    print("Congratulations Player2 YOU WON!")

def Remis():
    print("Well, it's a tie!")


player1 = Choose1()

while True:
    if player1 in ("1", "2", "3"):
        clear()
        break
    else:
        clear()
        print("Choose from 1 to 3!")
        player1 = Choose1()
        continue


player2 = Choose2()

while True:
    if player2 in ("1", "2", "3"):
        clear()
        break
    else:
        clear()
        print("Choose from 1 to 3!")
        player2 = Choose2()


if player1 == player2:
    Remis()
elif player1 == "1":
    if player2 == "2":
        Win2()
    elif player2 == "3":
        Win1()
elif player1 == "2":
    if player2 == "1":
        Win2()
    elif player2 == "3":
        Win1()
elif player1 == "3":
    if player2 == "1":
        Win2()
    elif player2 == "2":
        Win1()