def FindMax(sequence):
    maxElem, index = sequence[0], 0
    for i in range(len(sequence)):
        if sequence[i] >= maxElem:
            index = i
            maxElem = sequence[i]
    return index


inputSequence = list(map(int, input().split()))
indexToFind = FindMax(inputSequence)
print(inputSequence[indexToFind], indexToFind)
