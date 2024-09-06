num=int(input('Enter the number: '))
def factorial(num):
    if num in range(0, 2):
        return 1
    else:
        return num*factorial(num-1)

print(f"The factorial of {num} is {factorial(num)}")