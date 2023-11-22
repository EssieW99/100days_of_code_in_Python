#!/usr/bin/python3

"""calculates the BMI of a person"""

# get the weight
weight = input("Enter your weight in kg: ")
# get the height
height = input("Enter your height in m: ")
# calculate the BMI
bmi = (int(weight)) / (float(height) ** 2)
# print BMI
bmi_int = int(bmi)
print(bmi_int)
