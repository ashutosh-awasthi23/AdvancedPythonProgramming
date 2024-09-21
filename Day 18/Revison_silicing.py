def slice_string(s):
    if len(s)>5:
        #return s[:5]
        l=len(s)
        #return s[l-5:]
        h = int(len(s) / 2)

        if len(s)%2==0:
            return s[h-1:h+1]
        else:
            return s[h-1:h+2]


text=input("Enter the string")
print(slice_string(text))