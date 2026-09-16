# age(integer) 
# is_employed(boolean) 
# credit_score(integer) 
# annual_income(float) 
# has_collateral(boolean) 

age = int(input("Enter your age: "))
is_employed = bool(input("Are you employed? ") == "true")
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("How much is your annual income: "))
has_collateral = bool(input("Do you have collateral? ") == "true")


if age >= 21 and is_employed == True:
    if credit_score >= 750:
        if annual_income >= 100000:
            print("Approved at 4.5% interest")
        else:
            print("Approved at 5.0% interest")
    elif 600 <= credit_score < 750:
        if has_collateral == True:
            print("Approved at 7.0% interest")
        elif annual_income < 40000:
            print("Approved at 9.5% interest")
        else:
            print("Approved at 8.0% interest")
    else:
        print("Rejected: Credit score too low")
else:
        print("Rejected: Fails baseline criteria")