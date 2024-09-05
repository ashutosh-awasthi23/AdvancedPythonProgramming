# text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book"
# li=text.split()
# i=1
# while i<len(li):
#     li[i]="replaced"
#     i=i+2
# print(" ".join(li))


text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book".replace(
    ".", " ")

words = text.split()
for i in range(0, len(words), 2):
    # words[i].replace(words[i], "replaced")
    words[i] = "replaced"

print(words)
print(text)


