n = int(input())

for i in range(n):
    for j in range(1, n + 1, 1):
        if j % 2 == 0:
            print(n - i, end='')
        else:
            print(i + 1, end='')
    print()