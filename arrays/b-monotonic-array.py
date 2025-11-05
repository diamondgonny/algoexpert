# 문제 풀이 1
def isMonotonic(array):
    c = d = True
    for i in range(len(array) - 1):
        c = (c and array[i] <= array[i + 1])
        d = (d and array[i] >= array[i + 1])

    return c or d
