# 문제 풀이 1
def getNthFib(n):
    a, b = 0, 1
    if n == 1:
        return a
    for i in range(n - 2):
        a, b = b, a + b
    return b

# 문제 풀이 2
def getNthFib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
# n:1 -> 0 (0,1)    // 0
# n:2 -> 0,1 (1,1)    // 1
# n:3 -> 0,1,1 (1,2)    // 1
# n:4 -> 0,1,1,2 (2,3)    // 2
# n:5 -> 0,1,1,2,3 (3,5)    // 3
# ...

# 문제 풀이 3 (재귀)
# 이 재귀 방식은 이해는 직관적이지만 중복 호출로 시간이 많이 걸릴 수 있음
# 예: get(5) = get(3) + get(4) = (get(1)+get(2)) + (get(2)+get(3)) = (0+1) + (1+1) = 3
# 메모이제이션 재귀(예: @functools.lru_cache)로 이런 중복 호출 결과값(예: get(5))을 자동으로 캐싱하고 재사용할 수 있다고 함
# O(2^n) -> O(n)
def getNthFib(n):
    if n < 3:
        return n - 1
    return getNthFib(n - 2) + getNthFib(n - 1)
# n:1 -> 0              // base: return 1-1 = 0
# n:2 -> 1              // base: return 2-1 = 1
# n:3 -> 1 (= F1 + F2)  // get(1)+get(2) = 0+1 = 1
# n:4 -> 2 (= F2 + F3)  // get(2)+get(3) = 1+1 = 2
# n:5 -> 3 (= F3 + F4)  // get(3)+get(4) = 1+2 = 3
# ...
