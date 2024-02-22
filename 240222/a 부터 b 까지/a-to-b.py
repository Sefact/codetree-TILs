a, b = map(int, input().split())

for i in range(a, b+1):
    print(a, end=' ')
    if i % 2 == 1:
        a *= 2
    elif i % 2 == 0:
        a += 3

    if a > b:
        break