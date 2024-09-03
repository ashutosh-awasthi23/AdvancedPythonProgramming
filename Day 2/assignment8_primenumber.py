num = int(input("Enter the number "))
li = []
i = 2
while i <= num:
    flag = 0
    j = 2
    while j <= i//2:
        if i % j == 0 :
            flag = 1
            break
        j = j+1
    if flag == 0:
            li.append(i)
    i=i+1
print(li)