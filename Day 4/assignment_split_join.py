# text="Ram goes to the market"
# li=text.split(" ")
# print(li)
#
# text="Ram-goes-to-the-market"
# li2=text.split("-")
# print(li)
#
# s1=" ".join(li)
# s2="-".join(li2)
#
# print(s1)
# print(s2)

sentence = "Hi I am Aaryan Pal"
words = sentence.split()
print("Words: ", words)

custom_split = sentence.split('i')
print("Custom split with comma: ", custom_split)

joined = " ".join(words)
print("Joint sentence: ", joined)

custom_joined = ", ".join(words)
print("Joint sentence: ", custom_joined)










