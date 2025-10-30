# 문제 풀이 1
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    r, b = sorted(redShirtSpeeds), sorted(blueShirtSpeeds, reverse=fastest)
    return sum(list(map(max, r, b)))

# 문제 풀이 2
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    return sum(max(r, b) for r, b in zip(redShirtSpeeds, blueShirtSpeeds))

# 공간복잡도 O(n) -> O(1)
# sorted(...) -> .sort()
# sum('list') -> sum('generator')

# Python의 list.sort()는 Timsort를 사용하며 일부의 경우 최대 O(n)의 임시 버퍼가 필요할 수 있음
# 하지만 새 리스트를 생성하는게 아니고 제자리에서 정렬하므로, 일반적으로 추가 공간 복잡도는 O(1)로 간주됨
# (원본이 변경된다는 건 염두에 두자)
