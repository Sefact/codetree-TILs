n = int(input())

for i in range(1, 2 * n + 2):
    for j in range(1, 2 * n + 2):
        if i % 2 == 1 or j % 2 == 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()