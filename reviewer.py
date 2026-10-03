age =  int(input("Enter your Age: "))
monthly_revenue = float(input("Enter your Monthly Revenue: "))
credit_score = int(input("Enter Credit Score: "))
years_in_business = float(input("Enter the Years in business field: "))
has_defaults = bool(input("Defaults History: ")) == "True"
collateral_name = input("Collateral Name: ")
collateral_value = float(input("Collateral Value: "))

max_loan = 0 
base_fee = 0.0

if age >= 21 and years_in_business >=2 and has_defaults == False:
    print("Accepted:You can proceed to the next step.")
    if credit_score >= 720: 
        print("Your credit score is accepted.")
        max_loan = monthly_revenue * 3
        if monthly_revenue >= 50000:
            base_fee = max_loan * 0.015
            print("Your base fee rate is ",base_fee)
        else:
            base_fee = max_loan * 0.025
            print("Base fee rate is ",base_fee)
        if collateral_value >= max_loan: 
            print ("Your collateral is accepted.")
            surcharge = base_fee
            if collateral_value % 5000 != 0:
                surcharge += 250.00 
                print ("Your total base fee is", surcharge)
                print ("Your loan is approved,", max_loan)            
        else: 
            print ("Rejected: Insufficient collateral.")
    elif 620 <= credit_score < 720: 
        max_loan = monthly_revenue * 1.5
        if years_in_business >= 5:
            base_fee = max_loan * 0.02
            print("base fee rate is ",base_fee)
        else:
            base_fee = max_loan * 0.035
            print("base fee rate is ",base_fee) 
            collateral_name = input("Enter the name of your collateral: ")
            collateral_value = float (input("Enter the value of your collateral: "))
            if collateral_value >= max_loan: 
                print("Your collateral is accepted.")
                surcharge = base_fee
                if collateral_value % 5000 != 0:
                    surcharge += 250.00 
                    print("Your total base fee is", surcharge)
                    print("Your loan is approved,", max_loan)            
                else: 
                    print ("Rejected: Insufficient collateral.")
            else: 
                print ("Rejected: Insufficient collateral.")
    elif credit_score < 620: 
        print("Rejected: Credit score below requirement.")         
else:
    print("Rejected: High Risk Application or Ineligible Owner.")