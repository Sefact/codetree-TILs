n  = int(input())

for i in range(n):
    if i == 0 :
        for j in range(n):
            print('*', end=' ')
    elif i == n - 1:
        for j in range(n):
            print('*', end=' ')
    else:
        for j in range(n):
            if j == 0 or j == n - 1:
                print('*', end=' ')
            elif i > j:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    
    print()