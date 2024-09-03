num = int(input("Enter a number: "))
fact = 1
if num == 0:
    print("Factorial of '{}' is '1'".format(num))
else:
    for i in range(num, 0, -1):
        fact *= i
    print("Factorial of '{}' is '{}'".format(num, fact))

