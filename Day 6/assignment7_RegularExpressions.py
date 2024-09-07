import re
file=open('index.txt','r')
li=file.readlines()

for i in li:
    if re.findall(r'^start',i)==['start'] and re.findall(r'end$',i)==['end']:
        print(i)
