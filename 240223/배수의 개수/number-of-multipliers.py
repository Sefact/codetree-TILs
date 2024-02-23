cntA = 0
cntB = 0


for _ in range(10):
    n = int(input())
    if n % 3 == 0:
        cntA += 1
    if n % 5 == 0:
        cntB += 1

print(cntA, cntB)