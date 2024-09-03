age = int(input("Enter your age: "))

if age < 5 and age > 0:
    print("Free")
elif age in range(5,13):
    print("Rs. 5")
elif age in range(13,61):
    print("Rs. 10")
elif age > 60:
    print("Rs. 7")
else:
    print("Invalid")