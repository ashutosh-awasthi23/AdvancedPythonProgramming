li=["a","e","i","o","u","A","E","I","O","U"]

text="This is fun"
for i in text:
    if i in li:
        text=text.replace(i,"abc")
print(text)