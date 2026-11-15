#stair
stair = int(input("Enter the number of stairs: "))
for x in range(1, stair + 1):
    for y in range(x):
        print("*", end= " ")
    print()

#box
for x in range(5):
    for y in range(5):
        if x == 0 or y == 4 or x == 4 or y == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
