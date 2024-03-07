n = int(input())
cnt = 0
cntB = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(n - cnt):
            print('*', end=' ')
    else:
        for j in range(cnt + 1):
            print('*', end=' ')
        cnt += 1
    print()

for i in range(n):
    if i % 2 == 0:
        for j in range(n - cnt):
            print('*', end=' ')
    else:
        for j in range(i):
            print('*', end=' ')
        cnt -= 1
    # elif i % 2 != 0:
    #     for j in range(cnt - 1):
    #         print('*', end=' ')
    #     cnt -= 1
    print()