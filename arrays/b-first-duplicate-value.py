# 문제 풀이 1
def firstDuplicateValue(array):
    res = -1

    for idx in range(len(array)):
        ref_idx = abs(array[idx]) - 1
        if array[ref_idx] > 0:
            array[ref_idx] *= -1
        else:
            res = abs(array[idx])
            break

    return res


# 문제 풀이 1'
def firstDuplicateValue(array):
    for val in array:
        absVal = abs(val)
        if array[absVal - 1] < 0:
            return absVal
        array[absVal - 1] *= -1

    return -1
