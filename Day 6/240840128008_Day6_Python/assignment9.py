import  re
file=open("email.txt",'r')
li=file.read()
print(li)
print(re.findall(r'([0-9]{3})[0-9]{3}[0-9]{4}',li),)