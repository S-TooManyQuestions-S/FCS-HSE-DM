# Дан список, заполненный произвольными целыми числами.
# Найдите в этом списке два числа, произведение которых максимально. Выведите эти числа в порядке неубывания.
# Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.
# Скорость работы: O(n)


def findMaxPair(sequence):
    maxPos, secondMaxPos = 0, 0
    for i in sequence:
        if i >= maxPos:
            secondMaxPos = maxPos
            maxPos = i
        elif i > secondMaxPos:
            secondMaxPos = i
    return maxPos, secondMaxPos


def findMinPair(sequence):
    minNeg, secondMinNeg = 0, 0
    for i in sequence:
        if i <= minNeg:
            secondMinNeg = minNeg
            minNeg = i
        elif i < secondMinNeg:
            secondMinNeg = i
    return minNeg, secondMinNeg


def FindMaxMult(sequence):
    maxPos, secondMaxPos = findMaxPair(sequence)
    minNeg, secondMinNeg = findMinPair(sequence)

    amountP, amountN = 0, 0

    for i in sequence:
        if i > 0:
            amountP += 1
        elif i < 0:
            amountN += 1

    if amountP == amountN == 0:
        return 0, 0
    elif amountN < 2 and amountP < 2:
        if amountP + amountN == 2 == len(sequence):
            return minNeg, maxPos
        elif amountP == 1 and amountN == 0:
            return 0, maxPos
        elif amountN == 1 and amountP == 0:
            return minNeg, 0

    if maxPos * secondMaxPos > minNeg * secondMinNeg:
        return secondMaxPos, maxPos
    else:
        return minNeg, secondMinNeg


li = list(map(int, input().split()))
print(*FindMaxMult(li))