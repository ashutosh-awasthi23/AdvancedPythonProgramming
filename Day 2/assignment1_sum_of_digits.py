num = int(input("Enter a positive number: "))
sm = 0
if num < 0:
    print("It's not a positive number")
else:
    n = num
    while n > 0:
        d = n % 10
        sm += d
        n = n//10

print(f"Sum of the digits of '{num}' is '{sm}'")

