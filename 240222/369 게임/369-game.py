n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 or i == 3 or i == 6 or i == 9:
        print(0, end=' ')
    else:
        print(i, end=' ')