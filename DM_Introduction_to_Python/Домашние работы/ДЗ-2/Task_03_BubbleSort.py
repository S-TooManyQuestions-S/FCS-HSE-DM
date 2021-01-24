def BubbleSort(sequence):
    while not IsSorted(sequence):
        for i in range(len(sequence)-1):
            if sequence[i] < sequence[i+1]:
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
    return sequence


def IsSorted(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] < sequence[i+1]:
            return False
    return True


print(*BubbleSort(list(map(int, input().split()))))