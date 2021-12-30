for i in range(1, 6):
    for j in range(1, i):
        print(" ", end="")
    for k in range(((5 - i) * 2) + 1):
        print("*", end="")
    print()