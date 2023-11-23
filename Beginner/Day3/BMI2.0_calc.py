#!/usr/bin/python3

"""calculates one's BMI and interprets it"""

# get the weight
weight = input("Enter your weight in kg: ")

# get the height
height = input("Enter your height in m: ")

# calculate the BMI
bmi = (int(weight)) / (float(height) ** 2)

# print BMI
bmi_int = round(bmi)
if bmi_int < 18.5:
    print("Your BMI is {}, you are underweight".format(bmi_int))
elif bmi_int > 18.5 and bmi_int < 25:
    print("Your BMI is {}, you have a normal weight".format(bmi_int))
elif bmi_int > 25 and bmi_int < 30:
    print("Your BMI is {}, you are overweight".format(bmi_int))
elif bmi_int > 30 and bmi_int < 35:
    print("Your BMI is {}, you are obese".format(bmi_int))
else:
    print("Your BMI is {}, you are clinically obese".format(bmi_int))
