file = open("test.txt", 'r')
li1 = file.readlines()
file.close()


file2 = open("test2.txt",'r')
li2 = file2.readlines()
li1 = li1+li2

s = set(li1)
li = list(s)

file3 = open("test3.txt",'w')
file3.writelines(li)
