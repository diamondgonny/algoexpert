# 문제 풀이 1
def commonCharacters(strings):
    if len(strings) == 1:
        return list(strings[0])

    ret = strings[0]
    for s in strings:
        ret = findCommonCharacters(ret, s)
    return ret

def findCommonCharacters(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    common = set1.intersection(set2)
    return list(common)

# 문제 풀이 2 (/w 복기) : map(이터레이터), *(언패킹 연산자) 활용
def commonCharacters(strings):
    return list(set.intersection(*map(set, strings)))

# map(set, strings) → 각 문자열을 집합으로 변환해 이터레이터를 만듬
    # 예: ["apple", "ample"] → [{'a','p','l','e'}, {'a','m','p','l','e'}]
# set.intersection(*...) → *(언패킹 연산자)를 이용해 모든 집합의 교집합을 한 번에 구함
    # (set1 & set2 & set3... 와 같은 효과)
# list(...) → 결과를 리스트로 변환해 반환함
