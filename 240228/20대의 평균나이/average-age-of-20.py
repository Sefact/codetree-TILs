val = 0
cnt = 0

while True:
    n = int(input())

    if n >= 30:
        print(f'{val / cnt:.2f}')
        break
    else:
        val += n
        cnt += 1