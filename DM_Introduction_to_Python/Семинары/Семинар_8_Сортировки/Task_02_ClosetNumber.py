# Напишите программу, которая находит в массиве элемент, самый близкий по величине к  данному числу.


def BinarySearch(sequence, key, sizeArray):
    left = 0
    right = sizeArray - 1
    while right > left:
        middle = (left + right) // 2
        if sequence[middle] > key:
            right = middle - 1
        elif sequence[middle] < key:
            left = middle + 1
        elif sequence[middle] == key:
            return middle
    return left


inputSize = int(input())
inputSeq = sorted(list(map(int, input().split())))
inputKey = int(input())
print(inputSeq[BinarySearch(inputSeq, inputKey, inputSize)])
