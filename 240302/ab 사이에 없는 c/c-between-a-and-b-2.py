a, b, c = map(int, input().split())
val = False

for i in range(a, b + 1):
    if c % i != 0:
        val = True

if val == True:
    print('YES')
else:
    print('NO')