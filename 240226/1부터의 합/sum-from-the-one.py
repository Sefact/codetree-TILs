n = int(input())
val = 0

for i in range(n):
    if val + i > n:
        break;

    val += i

print(val)