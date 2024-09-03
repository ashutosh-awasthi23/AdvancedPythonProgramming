t = tuple(int(x) for x in input("Enter your tuple separated by commas: ").split())
t = sorted(t)
li=[]
element = int(input("Enter threshold elements"))
i=0
while i <len(t):
    if t[i] < element:
        e = t.pop(i)
        li.append(e)
    else:
        i=i+1
t=tuple(t)
print(f"The tuple is {t}")
print(f"The filtered element are {li}")




