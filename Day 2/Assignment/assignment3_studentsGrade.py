name=input("Enter the name: ")
homework=float(input("Enter the marks of homework out of 100 :"))
quizzes=float(input("Enter the marks of quizzes out of 100 :"))
midterm=float(input("Enter the marks of midterm out of 100 :"))
finalExam=float(input("Enter the marks of finalExam out of 100 :"))

total=(0.20*homework)+(0.20*quizzes)+(0.30*midterm)+(0.30*midterm)
print(total)
if total>90:
    print("The grade is A")
elif total>80 and total<90:
    print("The grade is B")
elif total>70 and total<80:
    print("The grade is C")
elif total>60 and total<70:
    print("The grade is D")
elif total>50 and total<60:
    print("The grade is F")

