student_name = input("Enter student name: ")
score1 = float(input("Enter score for Maths: "))
score2 = float(input("Enter score for Chemistry: "))
score3 = float(input("Enter score for Physics: "))

total_score = score1 + score2 + score3
average = total_score / 3

if average >= 70:
    grade = "A"
    remark = "Distinction"
elif average >= 60:
    grade = "B"
    remark = "Credit"
elif average >= 50:
    grade = "C"
    remark = "Pass"
elif average >= 40:
    grade = "D"
    remark = "Pass"
else:
    grade = "F"
    remark = "Fail"


print("       STUDENT RESULT REPORT       ")

print(f" Student Name : {student_name.title()}")

print(f" Subject 1    : {score1:}")
print(f" Subject 2    : {score2:}")
print(f" Subject 3    : {score3:}")
print(f" Total Score  : {total_score:} / 300")
print(f" Average Score: {average:.2f}%")
print(f" Final Grade  : {grade} ({remark})")