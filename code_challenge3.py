#Global Freight Calculator
a='yes'
b='yes'

Sender_Name = input("Enter Sender Name: ")
Type_of_Item = input("Enter Type of the item: ")
isFragile = input("The item is fragile?, YES OR NO: ")
Weight = float(input("Weight of the item {in kg}: "))
Distance = float(input("Distance in Shipping Place {in km}: "))
isExpress = input("Is the package need to expres?, YES OR NO: ")
isInternational = input("Is the package is international?, YES OR NO: ")


#Calculate Base Cost
base_cost = (Weight * 2.50) + (Distance * 0.15)

#Evaluate Pricing Tiers
if Weight <= 2 and Distance <= 100 and a != isExpress and b != isInternational:			print("TOTAL:₱ 0.00")

elif a == isExpress and b == isInternational:
	print("TOTAL AMOUNT:₱",base_cost * 1.40 + 50,)
	
elif a == isExpress or b == isInternational and Weight > 20:
	print("TOTAL AMOUNT:₱",base_cost * 1.20 + 25,)

elif Weight > 30 or Distance > 1000:
	print("TOTAL AMOUNT:₱",base_cost + 30,)

else:
	print("TOTAL AMOUNT:₱",base_cost,)


