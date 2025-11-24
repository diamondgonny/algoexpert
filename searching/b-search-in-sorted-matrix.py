# 문제 풀이 1
def searchInSortedMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1

    while i < len(matrix) and j >= 0:
        if target == matrix[i][j]:
            return [i, j]
        elif target < matrix[i][j]:
            j -= 1
        elif target > matrix[i][j]:
            i += 1

    return [-1, -1]
