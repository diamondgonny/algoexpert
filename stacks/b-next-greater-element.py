# 문제 풀이 1
def nextGreaterElement(array):
    l = len(array)
    stack = []  # next greater element를 가리키는 지표
    res = [-1] * l

    # circular array 어케 하지? -1 -> -1 - l 로 어쩌다 해결 (어이 털림)
    for i in range(l - 1, -1 - l, -1):
        while stack and stack[-1] <= array[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(array[i])

    return res
