n = int(input())

for i in range(1, n + 1, 1):
    if i == 1:
        for j in range(n):
            print('*', end=' ')
    else:
        for j in range(1, n + 1, 1):
            if j % 2 == 0 and i <= j:
                print('*', end=' ')
            else:
                print(' ', end=' ')

    print()