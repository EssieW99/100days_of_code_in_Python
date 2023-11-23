#!/usr/bin/python3

"""identifies if a year is a leap year or not"""

# inquire the year you want to check
year = int(input("Which year would you like to check? "))

#check if the year is a leap year or not
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
