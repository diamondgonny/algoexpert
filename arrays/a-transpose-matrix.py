# 문제 풀이 1
def transposeMatrix(matrix):
    return [list(r) for r in zip(*matrix)]

# zip(*A): 각 행을 개별 인자로 넘겨 열 단위로 묶기 때문에, 사실상 transpose의 핵심이 됨
    # zip은 여러 이터러블의 같은 위치 원소들을 튜플로 묶는 함수
    # *(언패킹) 연산자는 리스트/튜플 같은 시퀀스를 풀어버림: [[], []] -> [], []
