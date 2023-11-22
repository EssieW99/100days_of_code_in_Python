#!/usr/bin/python3

"""calculates how much one should pay plus the tip"""

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

# calculate the amount of the tip
tip_in_cash = (float(bill) * (int(tip) / 100))

# calculate the total amount plus the tip
total_bill = float(bill) + tip_in_cash

# calculate how much each person should pay
amount = total_bill / int(people)
amount_roundedoff = round(amount, 2)

# print
print("Each person should pay: ${:.2f}".format(amount_roundedoff))
