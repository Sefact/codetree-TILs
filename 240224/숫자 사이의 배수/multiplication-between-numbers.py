a, b = map(int, input().split())
val = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        val += i
        cnt += 1

print(val, f'{val / cnt:.1f}')