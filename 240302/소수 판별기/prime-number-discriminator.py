n = int(input())
val = False

for i in range(2, n):
    if n % i != 0:
        val = True
        break

if val == True:
    print('P')
else:
    print('C')