ti=tuple(int(x) for x in input("Enter the tuple integers: ").split())
num=int(input("Enter the number uh want to repeat: "))
if num not in ti:
    print("Entered number is not in tuple")
else:
    li=list(ti)
    id=li.index(num)
    num2=int(input("How many times you want to repeat? "))
    while num2-1:
        li.insert(id,num)
        num2=num2-1
t=tuple(li)
