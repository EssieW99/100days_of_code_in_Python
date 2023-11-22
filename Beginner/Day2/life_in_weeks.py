#!/usr/bin/python3

"""calculates how many weeks one has left
if they were to love to 90 years
"""

# get the current age
age = input("What is your current age: ")
# get years left
years = 90 - int(age)
# get months left
months = years * 12
# get weeks left
weeks = years * 52
# get days left
days = years * 365

# print result
print("You have {} days, {} weeks, {} months and {} years left".format(days, weeks, months, years))
