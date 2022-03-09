import random
print("Enter the marks of five subjects::")
subject_1 = float(random.randint(0.0,100.00))
print(subject_1)
subject_2 = float(random.randint(0.0,100.00))
print(subject_2)
subject_3 = float(random.randint(0.0,100.00))
print(subject_3)
subject_4 = float(random.randint(0.0,100.00))
print(subject_4)
subject_5 = float(random.randint(0.0,100.00))
print(subject_5)

total, percentage, grade = None, None, None

total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = (total / 500.0) * 100

if percentage >= 90 :
    grade = 'A'
elif percentage >= 80 :
    grade = 'B'
elif percentage >= 70 :
    grade = 'C'
elif percentage >= 60 :
    grade = 'D'
else:
    grade = 'E'

print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe Grade is:         \t", grade)