amount = float(input("Enter your bank account balance: "))

while True:
    while True:
        print("\n********** To withdraw money enter the amount in multiple of 10 ony **********\n")
        withdrawal_amount = int(input("Enter the withdrawal amount: "))

        if withdrawal_amount % 10 != 0:
            print("Enter amount in multiple of 10 only!! Try again.")

        else:
            break

    if withdrawal_amount > amount:
        print("Insufficient balance")

    else:
        amount = amount - withdrawal_amount
        print(f"Withdrawal is successful. Remaining amount is {amount}")

    a = input("Press Y/y to continue for more withdrawal: ")

    if a == 'Y' or a == 'y':
        continue
    else:
        break
