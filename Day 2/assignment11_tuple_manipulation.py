t = tuple(int(x) for x in input("Enter your tuple: ").split(','))

print("\nTuple: ", t)
print("First element of the tuple: ", t[0])
print("Last element of the tuple: ", t[-1])
print("Excluding first and last element of the tuple: ", t[1:-1])
print("Every second element of the tuple: ", t[::2])
print("Reversed tuple: ", t[-1::-1], "\n")

