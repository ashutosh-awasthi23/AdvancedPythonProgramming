dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2]}
invert = {value: key for key, value in dict1.items()}

print(invert)
