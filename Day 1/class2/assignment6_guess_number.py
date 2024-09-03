secret_number = 543
tries = 0
flag = 0
while tries < 10:
    n = int(input("guess the number: "))
    tries += 1
    if n == secret_number:
        print(f"Attempt {tries} You guessed right number")
        flag = 1
        break
    else:
        print(f"Attempt {tries} You guessed wrong number, Try again!")
if tries == 10 and flag == 0:
    print(f"Attempt {tries} You guessed wrong number for the last time as well, Hard luck")
