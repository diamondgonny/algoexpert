# 문제 풀이 1
def minimumWaitingTime(queries):
    queries = sorted(queries)
    n = len(queries)
    res = 0

    for i in range(n):
        res += queries[i] * (n - 1 - i)

    return res

#     [ 3, 2, 1, 2, 6] : how to calculate the minimum waiting time with it?
#  -> [ 1, 2, 2, 3, 6]
#      (0) + (1) + (1+2) + (1+2+2) + (1+2+2+3) = 17
