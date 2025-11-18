# 문제 풀이 1
# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    prevMax = array[0]                 # dp[i-2]
    crntMax = max(array[0], array[1])  # dp[i-1]
    for i in range(2, len(array)):
        prevMax, crntMax = crntMax, max(crntMax, prevMax + array[i])
    return crntMax
# dp[0] = array[0]
# dp[1] = max(array[0], array[1])
# dp[i] = max(dp[i-1], dp[i-2] + array[i])   (i ≥ 2)


# 문제 풀이 2
def maxSubsetSumNoAdjacent(array):
    prevMax = crntMax = 0
    for x in array:
        prevMax, crntMax = crntMax, max(crntMax, prevMax + x)
    return crntMax
