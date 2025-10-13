# 문제 풀이 1
def selectionSort(array):
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            # array[i] > array[j]: 로 작성하고 막혀서 5분 어리둥절;
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array
