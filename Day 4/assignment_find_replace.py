s = "This is a string. Having first first occurrence of words first and second and second"

search = 'first'
print(f"First occurrence of {search} at index: {s.find('first')}")

prev_occ = -1
print(f"Occurrences of string {search} at indexes:")
occ_list = []
for i in range(len(s)):
    prev_occ = s.find(search, prev_occ+1)
    if prev_occ == -1 and len(occ_list) != 0:
        break
    elif prev_occ == -1:
        print("Substring not present!!")
    else:
        occ_list.append(prev_occ)
print(occ_list, "\n")

# Replace first occurrence
s = s.replace("second", "third", 1)
print(s)

# Replace all occurrence
s = s.replace("first", "second")
print(s)

