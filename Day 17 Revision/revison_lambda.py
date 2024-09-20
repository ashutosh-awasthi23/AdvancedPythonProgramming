li=[('Mayura',30),('Pravin',25),('Reeya',35)]
sorted_by_age = sorted(li, key=(lambda x: x[1]))
print(sorted_by_age)