n = int(input())
val = True

for i in range(2, n):
    if n % i == 0:
        val = False
        break

if val:
    print('P')
else:
    print('C')