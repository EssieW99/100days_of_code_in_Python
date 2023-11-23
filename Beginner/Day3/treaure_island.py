#!/usr/bin/python3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure")
road = input("You are at a cross road. Which way will you go? Type 'left' or 'right' ").lower()
if road == 'left':
    river = input("You've come across an island in the middle of a lake. Will you swim or wait for the canoe? Type 'swim' or 'wait' ").lower()
    if river == 'wait':
        door = input("You're on the island. There are three houses. Which coloured door will you enter to retrieve the treasure? Type 'blue', 'yellow', or 'red ").lower()
        if door == 'red':
            print("You enter a room of beasts. Game Over")
        elif door == 'blue':
            print("You enter a room of with a dark hole. Game Over")
        elif door == 'yellow':
            print("You found the treasure. You Win!")
    else:
        print("You get eaten by a crocodile. Game Over")
else:
    print("You fall down a cliff. Game Over")
