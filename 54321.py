i = 6
while i > 0:
    for num in reversed(range(1, i)):
        print(num, end="")
    i -= 1
    print("\n")
