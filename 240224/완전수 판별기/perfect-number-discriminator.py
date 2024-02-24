n = int(input())
val = 0

for i in range(1, n+1):
    if n % i == 0 and i != n:
        val += i

if val == n:
    print('P')
else:
    print('N')