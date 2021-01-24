def LineSearch(sequence, seqSize, x):
    times = 0
    for i in range(seqSize):
        if sequence[i] == x:
            times += 1
    return times


inputSize = int(input())
inputSequence = list(map(int, input().split()))
inputElem = int(input())
print(LineSearch(inputSequence, inputSize, inputElem))