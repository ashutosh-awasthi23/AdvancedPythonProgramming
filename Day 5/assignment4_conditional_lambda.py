numbers = [10, -5, 0, 7, -3, 4, 2]
# li = map(lambda x: "zero" if x == 0 else "positive" if x >= 1 else "negative", numbers)
# print(list(li))

li=list(map(lambda  x:x**2,numbers))
print(li)