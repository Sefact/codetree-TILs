n = int(input())
val = False

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            val = True

if val == True:
    print('C')
else:
    print('N')