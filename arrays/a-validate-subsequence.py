# 문제 풀이 1
def isValidSubsequence(array, sequence):
    j = 0

    for i in array:
        if i == sequence[j]:
            j += 1
        if j == len(sequence):
            return True

    return False
