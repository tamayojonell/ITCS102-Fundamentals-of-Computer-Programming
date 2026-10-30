rows = int(input("Enter the number of rows: "))

for t in range(0, rows):
    for m in range(0, rows - t - 1):
        print(" ", end="")
    for m in range(0, t + 1):
        print("* ", end="")
    print()

for t in range(0, rows - 1):
    for m in range(0, t + 1):
        print(" ", end="")
    for m in range(0, rows - t - 1):
        print("* ", end="")
    print()
