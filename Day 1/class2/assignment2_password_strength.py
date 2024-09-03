password = input("Enter your password")
score = 0

specialCharacter = ['!', '@', "#", "$"]
if len(password) >= 8:
    score += 1
for j in l:


for i in password:
    if i.isdigit():
        score += 1
    if i in specialCharacter:
        score += 1






# password = input("Enter your password")
# score = 0
#l=list(password)
# specialCharacter = ['!', '@', "#", "$"]
# upper = [chr(num) for num in range(65, 91)]
# lower = [chr(num) for num in range(97, 123)]
# number = [chr(num) for num in range(48, 58)]
# if len(password) >= 8:
#     score = score + 1
#
# for i in password:
#     if i.
#     # if i in upper and i in lower:
#     #     score = score+1
#     # if i in number:
#     #     score = score+1
#     # if i in specialCharacter:
#     #     score = score+1
#
# if score == 4:
#     print("Strong Password")
# elif score == 2 or score == 3:
#     print("Moderate Password")
# elif score == 1:
#     print("Weak Password")