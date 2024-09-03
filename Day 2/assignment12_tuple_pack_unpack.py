name = input("Enter your name: ")
age = input("Enter your age: ")
address = tuple(x for x in input("Enter city and country separated by comma: ").split(', '))

details = (name, age, address)
print("Packed tuple: ", details)
a, b, c = details
city, country = c
print(f"Unpacked tuple:\nname--> {a}\nage--> {b}\ncity--> {city}\ncountry--> {country}")


