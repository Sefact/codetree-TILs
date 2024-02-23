n = int(input())

# 교실(2일)
a = 0
# 복도(3일)
b = 0
# 화장실(12일)
c = 0

for i in range(1, n):
    if i % 2 == 0 and i % 3 == 0:
        if a > b:
            b += 1
        elif b > a:
            a += 1
    elif i % 2 == 0 and i % 12 == 0:
        if a > c:
            c += 1
        elif c > a:
            a += 1
    elif i % 3 == 0 and i % 12 == 0:
        if b > c:
            c += 1
        elif c > b:
            b += 1
    else:
        if i % 2 == 0:
            a += 1
        elif i % 3 == 0:
            b += 1
        elif i % 12 == 0:
            c += 1

print(a, b, c)