#boolean variable

Tuloy = True

while Tuloy == True:
    ask = input("Do you want to continue? (yes/no): ")
    if ask.lower() == "yes":
        print("You chose to continue.")
        continue
    else:
        print("You chose to stop.")
        break
