# 문제 풀이 1 (XOR)
def missingNumbers(nums):
    xorAll = 0
    for i in range(1, len(nums) + 3):
        xorAll ^= i
    for x in nums:
        xorAll ^= x
    # xorAll = a ^ b

    mask = xorAll & -xorAll
    a = b = 0

    for i in range(1, len(nums) + 3):
        if i & mask:
            a ^= i
        else:
            b ^= i
    for x in nums:
        if x & mask:
            a ^= x
        else:
            b ^= x

    return [a, b] if a < b else [b, a]
    # 1. xorAll = (1^a^3^4^b)^(1^4^3) = a^b
    # 2. 우리가 (서로 다른 수인) a, b를 구하기 위해 mask로 활용한다.
    #    mask: xorAll(=a^b)에서 가장 낮은 1비트를 추출한 값
    # 3. a = (1^a^3)^(1^3) = 2, b = (4^b)^(4) = 5


# 문제 풀이 2 (인덱스 마킹)
def missingNumbers(nums):
    nums += [float("inf"),float("inf")]
    res = []

    for i in range(len(nums) - 2):
        v_i = abs(nums[i]) - 1
        nums[v_i] *= -1

    for i, num in enumerate(nums):
        if num > 0:
            res.append(i + 1)

    return res
