n = int(input())

# 교실(2일)
a = 0
# 복도(3일)
b = 0
# 화장실(12일)
c = 0

tempA = 0
tempB = 0
tempC = 0

for i in range(1, n+1):
    if i % 2 == 0 and i % 3 == 0 and i % 12 == 0:
        minVal = tempA
        if tempB < minVal:
            minVal = tempB
        if tempC < minVal:
            minVal = tempC

        if minVal == tempA:
            a += 1
            tempA = i
        elif minVal == tempB:
            b += 1
            tempB = i
        elif minVal == tempC:
            c += 1
            tempC = i
    elif i % 2 == 0 and i % 3 == 0:
        minVal = tempA
        if tempB < minVal:
            minVal = tempB
        
        if minVal == tempA:
            a += 1
            tempA = i
        elif minVal == tempB:
            b += 1
            tempB = i
    elif i % 2 == 0 and i % 12 == 0:
        minVal = tempA
        if tempC < minVal:
            minVal = tempC
        
        if minVal == tempA:
            a += 1
            tempA = i
        elif minVal == tempC:
            c += 1
            tempC = i
    elif i % 3 == 0 and i % 12 == 0:
        minVal = tempB
        if tempC < minVal:
            minVal = tempC
        
        if minVal == tempB:
            b += 1
            tempB = i
        elif minVal == tempC:
            c += 1
            tempC = i
    else:
        if i % 2 == 0:
            a += 1
            tempA = i
        elif i % 3 == 0:
            b += 1
            tempB = i
        elif i % 12 == 0:
            c += 1
            tempC = i

print(a, b, c)