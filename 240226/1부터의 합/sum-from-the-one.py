n = int(input())
val = 0

for i in range(n + 1):
    if val + i > n:
        break;

    val += i

print(i)