#!/usr/bin/python3

"""an automatic pizza order program"""

# get the pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

# calculation
total = 0
if size == 'S':
    if add_pepperoni == 'Y':
        total += 2
    else:
        total += 0
    if extra_cheese == 'Y':
        total += 1
    else:
        total += 0
    total += 15
elif size == 'M':
    if add_pepperoni == 'Y':
        total += 3
    else:
        total += 0
    if extra_cheese == 'Y':
        total += 1
    else:
        total += 0
    total += 20
elif size == 'L':
    if add_pepperoni == 'Y':
        total += 3
    else:
        total += 0
    if extra_cheese == 'Y':
        total += 1
    else:
        total += 0
    total += 25
print("The final bill is: ${}".format(total))
