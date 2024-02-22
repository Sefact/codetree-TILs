n = int(input())
t = False

for i in range(1, n + 1):
    if i % 3 == 0:
        print(0, end=' ')
    else:
        num = i
        while num > 0:
            multiple = num % 10
            if multiple == 3 or multiple == 6 or multiple == 9:
                t = True
                break
            num //= 10
        if t:
            print(0, end=' ')
        else:
            print(i, end=' ')