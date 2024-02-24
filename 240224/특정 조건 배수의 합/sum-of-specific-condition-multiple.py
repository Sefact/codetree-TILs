a, b = map(int, input().split())
val = 0

for i in range(a, b+1):
    if i % 5 == 0:
        val += i

print(val)