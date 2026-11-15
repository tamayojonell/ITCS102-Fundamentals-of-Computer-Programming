
isContinue = True
fruit = []

while isContinue == True:
    ask = input("Do you want to eat fruits? (yes/no): ")
    if ask.lower() == "yes":
        fruits = input("What fruits do you want to eat? ")
        fruit.append(fruits)
        answer = input("Do you want to eat more fruits? (yes/no): ")
        if answer.lower() == "yes":
            print("You chose to eat more fruits.")
            continue
        else:
            print("You chose to stop eating fruits.")
            break
    else:
        print(fruit)
