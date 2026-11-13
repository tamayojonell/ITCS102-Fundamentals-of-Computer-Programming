#TASK 1
print("TASK NUMBER 1")
print("\n")

loan = float(input("Enter the loan amount: $"))
years = int(input("Enter the loan period in years: "))

months = years * 12
interest_rate = 0.00256

principal = loan / months
remaining_loan = loan

print("\nPayment Schedule")
print("|\tMonth\t\t |\tMonthly Payment\t | \tInterest\t | \tPrincipal\t |\tRemaining Loan\t |")
print("--------------------------------------------------------------------------------------------------------------------------")

for x in range(months):
    interest = remaining_loan * interest_rate
    principal = principal
    if x == months - 1:
        principal = remaining_loan
    monthly_payment = principal + interest
    remaining_loan -= principal
    values = (x + 1, monthly_payment, interest, principal, remaining_loan)
    for y in range(5):
        if y == 0:
            print(f"|\t{values[y]}", end="\t\t |")
        else:
            print(f"\t${values[y]:.2f}", end="\t\t |")
    print()
print()



#TASK 2
print("TASK NUMBER 2")
print("\n")

for x in range(7):
    for y in range(13):
        if x + y == 6 or y - x == 6 or x == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()


#TASK 3
print("TASK NUMBER 3")
print("\n")

for x in range(6):
    for y in range(5):
        if x == 0 or x == 4 or x + y == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()
