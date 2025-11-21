# 문제 풀이 1
def sunsetViews(buildings, direction):
    res = []
    sunsetOk = 0

    if direction == "WEST":
        for i, v in enumerate(buildings):
            if sunsetOk < v:
                res.append(i)
                sunsetOk = v
    elif direction == "EAST":
        for i, v in enumerate(reversed(buildings)):
            if sunsetOk < v:
                res.append(len(buildings) - 1 - i)
                sunsetOk = v
        res.reverse()

    return res
