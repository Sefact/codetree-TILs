n = int(input())
val = 1

for i in range(1, n + 1):
    if val * i >= n:
        break

    val *= i

print(i)