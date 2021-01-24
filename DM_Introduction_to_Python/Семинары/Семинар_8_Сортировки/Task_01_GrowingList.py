# Дан список. Определите, является ли он монотонно возрастающим
# (то есть верно ли, что каждый элемент этого списка больше предыдущего).
# Выведите YES, если массив монотонно возрастает и NO в противном случае.


def IsAscending(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True


inputSeq = list(map(int, input().split()))

print("YES" if IsAscending(inputSeq) else "NO")
