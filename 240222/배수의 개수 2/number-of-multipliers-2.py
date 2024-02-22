arr = []
cnt = 0

for _ in range(10):
    num = int(input())
    arr.append(num)

for i in arr:
    if i % 2 == 1:
        cnt += 1

print(cnt)