n = int(input())
cnt = 0

for i in range(1, n):
    if i >= 400:
        if i % 4 == 0:
            cnt += 1

        if i % 4 == 0 and i % 100 == 0 and i %  400 != 0:
            cnt -= 1
    else:
        if i % 4 == 0:
            cnt += 1

print(cnt)