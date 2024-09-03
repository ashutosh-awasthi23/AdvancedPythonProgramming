while True:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    target = int(
        input("Press 1 for addition\n Press 2 for subtraction\n Press 3 for multiplication \n Press 4 for divison"))
    match target:
        case 1:
            print(f"The addition is {a + b}")

        case 2:
            print(f"The subtraction of b from a is {a - b}")

        case 3:
            print(f"The multiplication  is {a * b}")

        case 4:
            print(f"The divison is {a / b}")

        case _:
            print("Wrong choice entered")

    c = input("Enter Y/y to continue")
    if c == 'Y' or c == 'y':
        continue
    else:
        break