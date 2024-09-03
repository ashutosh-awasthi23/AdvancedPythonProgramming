
n = int(input("Enter number of rows"))
c = n+3
i = 1
while i <= n:
    j = 1
    while j <= c:
        if j >= 5-i and j <= 3+i:
            print("*",end=" ")
        else:
            print(end="  ")
        j=j+1
    i=i+1
    print()
