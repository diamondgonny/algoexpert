# 문제 풀이 1
def bestSeat(seats):
    idx = 0
    max_0 = 0
    tmp_idx = 0
    tmp_max_0 = 0

    for i in range(1, len(seats)):
        if seats[i - 1] and not seats[i]:  # 1 0
            tmp_idx = i
            tmp_max_0 = 1
        elif not seats[i - 1] and not seats[i]:  # 0 0
            tmp_max_0 += 1
        elif not seats[i - 1] and seats[i]:  # 0 1
            if max_0 < tmp_max_0:
                idx = tmp_idx
                max_0 = tmp_max_0

    return (idx - 1) + (max_0 + 1) // 2
