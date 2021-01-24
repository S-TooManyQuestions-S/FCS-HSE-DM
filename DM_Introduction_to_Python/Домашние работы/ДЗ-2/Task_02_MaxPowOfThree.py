def findMaxPair(li):
    maxPos, secondMaxPos, thirdMaxPos = findMinPair(li)
    for i in li:
        if i >= maxPos:
            thirdMaxPos = secondMaxPos
            secondMaxPos = maxPos
            maxPos = i
        elif i > secondMaxPos:
            thirdMaxPos = secondMaxPos
            secondMaxPos = i
        elif i > thirdMaxPos:
            thirdMaxPos = i
    return maxPos, secondMaxPos, thirdMaxPos


def findMinPair(li):
    minNeg, secondMinNeg, thirdNeg = 0, 0, 0
    for i in li:
        if i <= minNeg:
            secondMinNeg = minNeg
            minNeg = i
        elif i < secondMinNeg:
            thirdNeg = secondMinNeg
            secondMinNeg = i
        elif i < thirdNeg:
            thirdNeg = i
    return minNeg, secondMinNeg, thirdNeg


def FindMaxMult(li):
    maxPos, secondMaxPos, thirdMaxPos = findMaxPair(li)
    minNeg, secondMinNeg, thirdMinNeg = findMinPair(li)

    amountP, amountN = 0, 0

    for i in li:
        if i > 0:
            amountP += 1
        elif i < 0:
            amountN += 1

    if amountP == 0:
        return findMaxPair(li)

    if len(li) <= 3:
        return [_ for _ in li]

    if maxPos * secondMaxPos*thirdMaxPos > minNeg * secondMinNeg*maxPos:
        return secondMaxPos, maxPos, thirdMaxPos
    else:
        return minNeg, secondMinNeg, maxPos


li = list(map(int, input().split()))
print(*FindMaxMult(li))