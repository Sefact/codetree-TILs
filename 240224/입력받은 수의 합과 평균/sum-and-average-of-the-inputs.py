n = int(input())
val = 0

for _ in range(n):
    num = int(input())
    val += num

print(val, f'{val / n:.1f}')