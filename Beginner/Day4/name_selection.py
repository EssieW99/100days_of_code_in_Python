#!/usr/bin/python3
import random
"""split string method"""


names_string = input("Give everyone's names, separated by a comma. ")
names = names_string.split(", ")
no_of_names = len(names)
random_choice = random.randint(0, no_of_names - 1)
person_who_pays = names[random_choice]
print("{} will pay for the meal today!".format(person_who_pays))
