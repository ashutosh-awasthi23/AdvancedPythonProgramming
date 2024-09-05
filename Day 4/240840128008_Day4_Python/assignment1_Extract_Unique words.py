text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book"
li=text.split()
for i in range(0,len(li)):
    if li[i].isalpha():
        li[i]=li[i].lower()

    if li[i].endswith(".") or li[i].endswith(','):
        s=li[i][:-1]
        li[i]=s
        print(s)
print(sorted(set(li)))