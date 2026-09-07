#import demo
import getpass #folder

username = "Jon_jon18"
password = "hay_Buhay333"

j = input("Input Username:")
k = getpass.getpass("Input Password:")

if j == username and k == password:
	print("Username and password are Correct!")

else:
	print("Access Denied")