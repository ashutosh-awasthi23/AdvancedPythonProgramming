import csv
students=[{"id":1,"Name":"Ram","age":20,"grade":"A"},{"id":2,"Name":"Shyam","age":20,"grade":"B"}]
file=open("students.csv",'w')
fieldnames=students[0].keys()
writer=csv.DictWriter(file,fieldnames=fieldnames)
writer.writeheader()
writer.writerows(students)
