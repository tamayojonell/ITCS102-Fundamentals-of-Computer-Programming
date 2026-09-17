# age(integer) 
# is_employed(boolean) 
# credit_score(integer) 
# annual_income(float) 
# has_collateral(boolean) 

print("****************LOGIN INFORMATION****************")
print("Please enter your username and password to proceed with the loan application.")
Username = input("Username: ")
Password = input("Password: ")
print("*************************************************")
print("Please enter again your username and password to confirm your login information.")
Username1 = input("Username: ")
Password1 = input("Password: ")

if Username == Username1 and Password == Password1:
    print("Login successful!")
    print("*************************************************")
    print("****************AGE****************")
    Age = int(input("Please enter your age: "))

    if  Age <= 65 and Age >= 21:
        print("You are eligible to apply for a loan.")
        print("**************NEXT STEP**************")
        print("Please enter the following information to determine your loan eligibility and interest rate.")
        Type = input("Please enter the type of collateral you have (if any): ")
        Value = float(input("Please enter the value of your collateral (if any): "))

        if Value > 30000:
            print("You have sufficient collateral to proceed with the loan application.")

            Amount = int(input("Please enter the amount you wish to loan: "))
            
            print("**************LOAN APPLICATION FORM**************")
            age = int(input("Enter your age: "))
            is_employed = bool(input("Are you employed? ") == "true")
            credit_score = int(input("Enter your credit score: "))
            annual_income = float(input("How much is your annual income: "))
            has_collateral = bool(input("Do you have collateral? ") == "true")


            if age >= 21 and is_employed == True:
                if credit_score >= 750:
                    if annual_income >= 100000:
                        print("Approved at 4.5% interest")
                        print("AMOUNT OF INTEREST: ₱", Amount * 0.045,)
                        print("TOTAL AMOUNT, ₱",Amount + (Amount * 0.045)) 
                    else:
                        print("Approved at 5.0% interest")
                        print("AMOUNT OF INTEREST: ₱", Amount * 0.05,)
                        print("TOTAL AMOUNT, ₱",Amount + (Amount * 0.05)) 
                elif 600 <= credit_score < 750:
                    if has_collateral == True:
                        print("Approved at 7.0% interest")
                        print("AMOUNT OF INTEREST: ₱", Amount * 0.07,)
                        print("TOTAL AMOUNT, ₱",Amount + (Amount * 0.07)) 
                    elif annual_income < 40000:
                        print("Approved at 9.5% interest")
                        print("AMOUNT OF INTEREST: ₱", Amount * 0.095,)
                        print("TOTAL AMOUNT, ₱",Amount + (Amount * 0.095)) 
                    else:
                        print("Approved at 8.0% interest")
                        print("AMOUNT OF INTEREST: ₱", Amount * 0.08,)
                        print("TOTAL AMOUNT, ₱",Amount + (Amount * 0.08)) 
                else:
                    print("Rejected: Credit score too low")
            else:
                    print("Rejected: Fails baseline criteria")  
        else:
            print("Collateral value is invalid. You may not be eligible for a loan.")
    else:
        print("You are not eligible to apply for a loan due to age restrictions.")
else:
    print("Login failed. You cannot proceed with the loan application. Please check your username and password.")
