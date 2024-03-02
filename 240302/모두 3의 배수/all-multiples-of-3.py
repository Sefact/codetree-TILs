val = True

for i in range(5):
    n = int(input())
    if n % 3 != 0:
        val = False

if val:
    print(1)
else:
    print(0)