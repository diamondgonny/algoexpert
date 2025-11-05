# 문제 풀이 1
def moveElementToEnd(array, toMove):
    i = 0
    cnt = 0
    while (cnt < len(array) - 1):
        if array[i] == toMove:
            array.pop(i)
            array.append(toMove)
        else:
            i += 1
        cnt += 1

    return array
# 시간복잡도 O(n * n)... <- while, pop


# 문제 풀이 2
def moveElementToEnd(array, toMove):
    p = 0
    for i in range(len(array)):
        if array[i] != toMove:
            array[i], array[p] = array[p], array[i]
            p += 1

    return array
# 투포인터(정방향) : 시간복잡도 O(n)
# 빨간 블럭, 파란 블럭 스왑해서 분류한다고 생각하였음


# 문제 풀이 2' (투포인터지만 보조포인터를 역방향으로도 사용O)
# left →                                     ← right
