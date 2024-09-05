s1="dalad ii dalad"
s2=s1[::-1]
if s1==s2:
    print("The string is palindrome")
else:
    print("It is not")

s2=list(s1)
for i in s2:
    if i==" ":
        s2.remove(i)
    if i.isalpha():
        i=i.lower()
s3="".join(s2)
print(s3)

