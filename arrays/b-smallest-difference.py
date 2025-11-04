# 문제 풀이 1
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    target = (float('inf'), float('-inf'))
    i = j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        tmp = abs(arrayOne[i] - arrayTwo[j])
        if tmp < abs(target[0] - target[1]):
            target = (arrayOne[i], arrayTwo[j])
        if arrayOne[i] > arrayTwo[j]:
            j += 1
        else:
            i += 1

    return [target[0], target[1]]


# 문제 풀이 2 (가독성만 좋아짐;)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    min_diff = float('inf')
    result = []
    i = j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        diff = abs(arrayOne[i] - arrayTwo[j])
        if diff < min_diff:
            min_diff = diff
            result = [arrayOne[i], arrayTwo[j]]
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1

    return result
