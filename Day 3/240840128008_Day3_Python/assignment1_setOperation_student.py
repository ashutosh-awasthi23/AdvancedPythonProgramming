math={'alice','bob','charlie','david'}
science={'charlie','david','eve','frank'}

print(f"The union of two sets is {math.union(science)}")
print(f"The intersection of two sets is{math.intersection(science)}")
print(f"The student in science but not in maths {science-math}")
print(f"The students in math but not in science {math-science}")
