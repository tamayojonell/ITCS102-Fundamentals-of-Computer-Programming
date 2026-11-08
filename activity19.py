from getpass import getpass
isLogin = False
LoginAttempt = 0

URN = "itzzmejo_26"
PWRD = "jo123"

while isLogin == False:
    Username = input("Enter your username: ")
    Password = getpass("Enter your password: ")
    if Username == URN and Password == PWRD:
        print("Login Successful!")
        print("Total Login Attempt: ", LoginAttempt)
        isLogin = True
    else:
        print("Login Failed. Incorrect username and password.")
        LoginAttempt += 1
        isLogin = False