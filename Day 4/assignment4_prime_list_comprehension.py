#  Aaryan Pal
# def is_prime(x):
#     flag = 0
#     for i in range(2, (x // 2) + 1):
#         if x % i == 0:
#             flag = 1
#     if flag == 1:
#         return 0
#     else:
#         return 1
#
#
# li = [x for x in range(2, 51) if is_prime(x)]
# print("Prime list: ", li)




#Ashutosh Awasthi
def isprime(x):
    flag=0
    for i in range(2 , x//2+1):
        if x % i == 0:
            flag = 1
    if flag != 1:
        return True
    else:
        return False

li = [x for x in range(2,50) if isprime(x)]
print(f"The list of prime number between 1 to 50 is{li}")



