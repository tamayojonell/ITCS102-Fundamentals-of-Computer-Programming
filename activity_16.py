stair = int(input("Enter the number of stairs: "))

for x in range(1, stair + 1):
    for y in range(x):
        print("*", end= " ")
    print()
