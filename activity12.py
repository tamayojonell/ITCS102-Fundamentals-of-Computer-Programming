#multiple if and elif conditions
 
#Create a python  program that would capture age group

print("=============AGE GROUP=============")

name = input("Enter Name:")
age = int(input("Enter Age:"))

if age >= 0 and age <= 5 :
	print("That age is considered as INFANT")

elif age >= 6 and age <= 12 :
	print("That age is considered as KID")

elif age >= 13 and age <= 15 :
	print("That age is considered as PRE TEEN")

elif age >= 16 and age <= 19 :
	print("That age is considered as TEENAGER")

elif age >= 20 and age <= 29 :
	print("That age is considered as EARLY ADULT")

elif age >= 30 and age <= 58 :
	print("That age is considered as ADULT")

elif age >= 59 and age <= 150 :
	print("That age is considered as SENIOR")


else:
	print("Age Invalid")

