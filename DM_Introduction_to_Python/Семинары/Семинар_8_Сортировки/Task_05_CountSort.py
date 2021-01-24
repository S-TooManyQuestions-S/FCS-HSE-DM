# Дан список из N (N ≤ 2 * 10^5) элементов,которые принимают целые значения от 0 до 100.
# Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
# СОРТИРОВКА ПОДСЧЕТОМ


def CountSort(sequence, maxValue):
    counter = [0 for _ in range(maxValue + 1)]
    sortedSeq = []
    for i in sequence:
        counter[i] += 1
    for i in range(maxValue + 1):
        sortedSeq.extend([i for _ in range(counter[i])])
    return sortedSeq


print(*CountSort(list(map(int, input().split())), 100))

