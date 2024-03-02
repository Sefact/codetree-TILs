a, b, c = map(int, input().split())
val = False

for i in range(a, b + 1):
    if i % c == 0:
        val = True
        break

if val == True:
    print('NO')
else:
    print('YES')