n = int(input())
cnt = 0

for i in range(1, n):
    if n <= 1:
        break
    else:
        cnt += 1
        n = n // i

print(cnt)