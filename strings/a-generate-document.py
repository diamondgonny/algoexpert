# 문제 풀이 1
def generateDocument(characters, document):
    a = {}

    for i in characters:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1

    for i in document:
        if i not in a or a[i] == 0:
            return False
        a[i] -= 1

    return True

# 문제 풀이 2 (/w 복기)
from collections import Counter
def generateDocument(characters, document):
    return Counter(document) - Counter(characters) == {}

# collections 모듈의 Counter를 써서 문제를 쉽게 해결할 수도 있음 (Counter가 뭔지 배움)
# Counter는 각 원소가 몇 번 등장했는지를 세어주는 딕셔너리형 객체임
