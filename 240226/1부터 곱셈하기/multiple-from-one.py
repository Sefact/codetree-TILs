n = int(input())
val = 1

for i in range(1, n):
    if val * i > n:
        break

    val *= i

print(i)