# 문제 풀이 1 (노양심 코드, 어차피 시간복잡도 O(nlogn))
def sortedSquaredArray(array):
    return sorted([i**2 for i in array])

# 문제 풀이 2 (two pointer)
# 두 개의 인덱스(포인터)로 배열/리스트 문제를 시간복잡도 O(n)으로 해결
def sortedSquaredArray(array):
    n = len(array)
    res = [0] * n
    l = 0
    r = n - 1

    for i in range(n - 1, -1, -1):
        l_sq = array[l] ** 2
        r_sq = array[r] ** 2

        if l_sq < r_sq:
            res[i] = r_sq
            r -= 1
        else:
            res[i] = l_sq
            l += 1

    return res
