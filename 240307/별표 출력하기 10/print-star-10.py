n = int(input())

for i in range(n * 2):
    if i % 2 == 0 and i != 0:
        for j in range(1 + int(i / 2)):
            print('*', end=' ')
    elif i % 2 == 1:
        for j in range(n - int((i - 1) / 2)):
            print('*', end=' ')
    elif i == 0:
        print('*', end='')
    print()