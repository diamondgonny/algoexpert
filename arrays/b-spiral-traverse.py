# 문제 풀이 1
def spiralTraverse(array):
    res = []
    t, b = 0, len(array) - 1
    l, r = 0, len(array[0]) - 1

    while l <= r and t <= b:
        res.extend(array[t][l:r + 1])
        t += 1
        res.extend(array[i][r] for i in range(t, b + 1))
        r -= 1
        if t <= b:
            res.extend(reversed(array[b][l:r + 1]))
            b -= 1
        if l <= r:
            res.extend(array[i][l] for i in range(b, t - 1, -1))
            l += 1

    return res

# res.extend
