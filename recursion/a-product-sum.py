# 문제 풀이 1
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    total = 0
    for item in array:
        if isinstance(item, list):
            total += productSum(item, depth + 1)  # 여기에 return을 넣고 잠시 헤맸음;
        else:
            total += item
    return depth * total

# 문제 풀이 2
# 사실 이래도 명시적 for 루프 대비 성능상 유의미한 이득이 거의 없다.  # 둘 다 O(n), 메모리 O(1)
    # sum(...) 안은 제너레이터 표현식이다.  # gen = (...), sum(gen)
    # 이 문제는 per-item 비용( isinstance + 경우에 따른 재귀 호출 )이 커서,
    # 제너레이터의 next()/프레임 중단·재개 오버헤드 이점이 상쇄된다.
def productSum(array, depth=1):
    return depth * sum(
        productSum(item, depth + 1) if isinstance(item, list) else item
        for item in array
    )
