# 문제 풀이 1
def arrayOfProducts(array):
    res = [1] * len(array)

    p = 1
    for i in range(len(array)):
        res[i] *= p
        p *= array[i]

    p = 1
    for i in reversed(range(len(array))):
        res[i] *= p
        p *= array[i]

    return res
