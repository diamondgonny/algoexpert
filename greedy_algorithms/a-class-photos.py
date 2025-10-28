# 문제 풀이 1
def classPhotos(redShirtHeights, blueShirtHeights):
    if sum(redShirtHeights) < sum(blueShirtHeights):
        front, back = redShirtHeights, blueShirtHeights
    else:
        front, back = blueShirtHeights, redShirtHeights

    front, back = sorted(front), sorted(back)

    for i in range(len(front)):
        if front[i] >= back[i]:
            return False

    return True


# 문제 풀이 2
def classPhotos(redShirtHeights, blueShirtHeights):
    r, b = sorted(redShirtHeights), sorted(blueShirtHeights)
    return all(x < y for x, y in zip(r, b)) or all(x > y for x, y in zip(r, b))
