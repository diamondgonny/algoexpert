# 문제 풀이 1
def mergeOverlappingIntervals(intervals):
    intervals.sort()
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if res[len(res) - 1][1] < intervals[i][0]:
            res.append(intervals[i])
        elif res[len(res) - 1][1] > intervals[i][1]:
            pass
        else:
            res[len(res) - 1][1] = intervals[i][1]

    return res


# 문제 풀이 1'
def mergeOverlappingIntervals(intervals):
    intervals.sort()
    res = [intervals[0]]

    for start, end in intervals[1:]:
        res_end = res[-1][1]
        if start > res_end:
            res.append([start, end])
        else:
            res[-1][1] = max(end, res_end)

    return res
