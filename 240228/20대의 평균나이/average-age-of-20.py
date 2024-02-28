val = 0
cnt = 0

while True:
    n = int(input())

    if 20 <= n <= 29:
        val += n
        cnt += 1
    else:
        print(f'{val / cnt:.2f}')
        break