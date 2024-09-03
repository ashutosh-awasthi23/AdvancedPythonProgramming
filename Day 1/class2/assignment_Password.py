hasspecialChar=False
hasDigit=False
hasUpper=False
hasLower=False

def strengthChecker():
    global hasspecialChar, hasDigit, hasUpper, hasLower
    for i in password:
        if i.isupper():
            hasUpper=True
        elif i.islower():
            hasLower=True
        elif i.isdigit():
            hasDigit=True
        elif i in special_characters:
            hasspecialChar=True


def strengthCalculator():
    strength=0
    if len(password)>=8:
        strength=strength+1
    if hasspecialChar:
        strength+=1
    if hasLower and hasUpper:
        strength+=1
    if hasDigit:
        strength+=1
    return strength



password=input("Enter the password")
special_characters = [
    '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',',
    '.', '/', '?', '~', '`', '!', ' ', '\t', '\n'
]


strengthChecker()
print(f"The strength of the password is{strengthCalculator()}")
