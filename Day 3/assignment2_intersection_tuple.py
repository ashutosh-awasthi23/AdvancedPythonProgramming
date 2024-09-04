t1 = tuple(int(x) for x in input("Enter tuple 1 values: ").split(','))
t2 = tuple(int(x) for x in input("Enter tuple 2 values: ").split(','))
s1 = set(t1)
s2 = set(t2)
print("Common elements: ", s1.intersection(s2))

