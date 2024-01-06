#!/usr/bin/python3
student_scores = input("Input a list of student's scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
maximum = student_scores[0]
for score in student_scores:
    if score > maximum:
        maximum = score
print("The highest score is {}".format(maximum))
