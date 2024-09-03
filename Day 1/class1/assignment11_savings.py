income = float(input("Enter your monthly income: "))
expense = float(input("Enter your total monthly expense: "))

total_savings = income - expense
saved_per = (total_savings/income) * 100

print("Total savings: ", total_savings)
print("Percentage of income saved: ", saved_per, "%")
print(f"Percentage of income spent: ", 100 - saved_per, "%")
