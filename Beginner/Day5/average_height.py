#!/usr/bin/python3
students_heights = input("Input a list of students' heights ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)
count = 0
sum = 0
for height in students_heights:
    count += 1
    sum += height
average = round(sum / count)
print("The average height is {}".format(average))
