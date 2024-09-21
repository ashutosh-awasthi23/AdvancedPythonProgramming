li1=[ x for x in input("Enter the list :").split(",")]
li2=[]
try:
    for i in li1:
        if not i.isdigit():
            raise ValueError("The entered value can not be converted to Integer")
    li2=[int(i) for i in li1]
except ValueError as ve:
    print(ve)
print(li2)