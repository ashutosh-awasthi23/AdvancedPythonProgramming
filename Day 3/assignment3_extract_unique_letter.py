# para = input("Enter the text: ")
# unique_letter = set(para)
# lst = [x for x in para.split(' ')]
# unique_words = set(lst)
# sorted_words = sorted(unique_words)
# sorted_letters = sorted(unique_letter)
#
# print("Sorted unique words: ", sorted_words)
# print("Sorted unique letters: ", sorted_letters)

















a=input("Enter the line or paragraph you wnat to enter :")
li=[]
for i in a:
    if i.isupper():
        i=i.lower()
    li.append(i)
s1=set(li)
s1.remove(" ")
li=sorted(s1)
print(f"The unique elements in text are {li}")