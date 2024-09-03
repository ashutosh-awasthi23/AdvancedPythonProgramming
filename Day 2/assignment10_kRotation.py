k = int(input("Enter the number of rotation: "))
li = [int(x) for x in input().split()]
k = k % len(li)
print(f"Before rotation{li}")
while k:
    temp = li[-1]
    j = len(li) - 2
    while j >= 0:
        li[j+1] = li[j]
        j = j-1
    li[0] = temp
    k = k-1
print(f"After rotation{li}")





