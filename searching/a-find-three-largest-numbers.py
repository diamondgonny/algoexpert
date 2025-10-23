# 문제 풀이 1
def findThreeLargestNumbers(array):
    v3 = v2 = v1 = float('-inf')
    for n in array:
        if v1 < n:
            v3 = v2
            v2 = v1
            v1 = n
        elif v2 < n:
            v3 = v2
            v2 = n
        elif v3 < n:
            v3 = n
    return [v3, v2, v1]


# 문제 풀이 2
def findThreeLargestNumbers(array):
    v3 = v2 = v1 = float('-inf')
    for n in array:
        if v1 < n:
            v3, v2, v1 = v2, v1, n
        elif v2 < n:
            v3, v2 = v2, n
        elif v3 < n:
            v3 = n
    return [v3, v2, v1]

# L22 보충 설명:
# 오른쪽을 먼저 평가해서 (v2, v1, n)이라는 튜플을 만든다.
# 그걸 왼쪽의 변수 세 개에 한 번에 풀어서(unpack) 각각 할당한다.
