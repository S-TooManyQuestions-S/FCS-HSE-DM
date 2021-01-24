def InsertionSort(sequence):
    for i in range(1, len(sequence)):
        # элемент для вставки
        toInsert = sequence[i]
        # предыдущий индекс
        j = i - 1
        # пока элементы больше нашего элемента для вставки - сдвигаем массив
        while j >= 0 and sequence[j] > toInsert:
            sequence[j + 1] = sequence[j]
            j -= 1
        # непосредственно вставка на нужное место
        sequence[j + 1] = toInsert
    return sequence


print(*InsertionSort(list(map(int, input().split()))))
