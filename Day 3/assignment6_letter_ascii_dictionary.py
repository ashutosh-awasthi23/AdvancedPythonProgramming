li = []
for i in range(97,102):
    li.append(chr(i))
dicto=dict.fromkeys(li,0)
for key,value in dicto.items():
    dicto[key]=ord(key)
print(dicto)


# dict1 = {}
# for i in range(ord('a'), ord('f')):
#     dict1[chr(i)] = i
# print(dict1)
