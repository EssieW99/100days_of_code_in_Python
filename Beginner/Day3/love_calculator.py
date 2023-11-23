#!/usr/bin/python3

"""tests the compatibility between two people"""

# get the names of two people
print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

# convert the name to lowercase
name1_lower = name1.lower()
name2_lower = name2.lower()
combined_string = name1_lower + name2_lower
# count the instances
t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t + r + u + e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

love = l + o + v + e
score = int(str(true) + str(love))

if (score) < 10 or (score) > 90:
    print("Your score is {}, you go together like coke and mentos".format(score))
elif (score) >= 40 and (score) <= 50:
    print("Your score is {}, you are alright together".format(score))
else:
    print("Your score is {}".format(score))
