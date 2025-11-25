# 문제 풀이 1
def threeNumberSort(array, order):
    a, b = 0, len(array) - 1

    for num in order:
        while a <= b:
            if array[a] == num:
                a += 1
            elif array[b] != num:
                b -= 1
            else:
                array[a], array[b] = array[b], array[a]
        b = len(array) - 1

    return array
