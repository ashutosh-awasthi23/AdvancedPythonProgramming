import re
# text="1234a5678b9aaa"
# print(re.findall(r'\d+\D', text))

file = open("index.txt", 'r')
li = file.readlines()
for i in li:
    # if re.findall(r'^Note', i) == ['Note'] and re.findall(r'!$', i) == ['!']:
    if re.match(r'^Note.*!$', i):
        print(i)

