a, b = map(int, input().split())
val = 0

if a < b:
    for i in range(a, b+1):
        if i % 5 == 0:
            val += i
elif a > b:
    for i in range(b, a+1):
        if i % 5 == 0:
            val += i

print(val)