# 문제 풀이 1
def threeNumberSum(array, targetSum):
    array.sort()
    result = []

    for i in range(len(array) - 2):
        l = i + 1
        r = len(array) - 1
        while (l < r):    # 내부 반복문: 투포인터 (중복 숫자x)
            if targetSum - array[i] == array[l] + array[r]:
                result.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif targetSum - array[i] > array[l] + array[r]:
                l += 1
            else:
                r -= 1

    return result
