# n = int(input("Input number of students: "))
# lst = []
# for i in range(n):
#     name, a, sc1, sc2, sc3 = input(f"Input student {i} data:").split(',')
#     age = int(a)
#     s1 = int(sc1)
#     s2 = int(sc2)
#     s3 = int(sc3)
#
#     s_tuple = (name, age, s1, s2, s3)
#     lst.append(s_tuple)
#
# print("All student data: ", lst)
#
# # Calculate average score of students
# highest = 0
# prev_high = 0
# for i in range(n):
#     # unpacking tuples
#     name, age, s1, s2, s3 = lst[i]
#     avg_score = (s1 + s2 + s3) / 3
#     # pack new tuple
#     new_tuple = (name, age, s1, s2, s3, avg_score)
#     lst[i] = new_tuple
#     # highest score
#     if avg_score > prev_high:
#         highest = i
#         prev_high = avg_score
#
# print("Updated list: ", lst)
# print(f"Student {highest} has highest score: {prev_high}")
# minimum = int(input("Input Minimum avg score: "))
# for i in range(n):
#     if lst[i][5] >= minimum:
#         print(lst[i][0], lst[i][5])























n  = int(input("Input the number of students: "))
pm = int(input("Enter the passing marks out of 100: "))
db =[tuple(y for y in input("Enter the details of student").split(',')) for x  in range(n)]
maxi =[]
db1=[]
for i in range(0,len(db)):
    db1.append(list(db[i]))
    avgscore = (int(db1[i][2])+int(db1[i][3])+int(db1[i][4]))/3
    maxi.append(avgscore)
    db1[i].append(avgscore)
    db1[i] = tuple(db1[i])
highest = maxi.index(max(maxi))
print(f"The details of Student with highest marks are{db1[highest]}")
print("The student which passed the exams are as follows :")
for i in range(0,len(db)):
    if int(db[i][-1])>pm:
        print(db1[i])



















