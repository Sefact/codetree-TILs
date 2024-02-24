val = 0
cnt = 0

for _ in range(10):
    n = int(input())
    if 0 <= n <= 200:
        val += n
        cnt += 1

print(val, f'{val / cnt:.1f}')