# 문제 풀이 1
def findClosestValueInBst(tree, target):
    closest = tree.value
    while tree is not None:
        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value
        if target < tree.value:
            tree = tree.left
        else:
            tree = tree.right
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BST의 특성을 활용하여 target과 가장 가까운 수(=closest) 찾기
    # 동일한 숫자 사용 가능; 우측 가지에 놓을 수 있음
# 조건에 따라 left/right를 선택하고 가지를 쭉 거슬러 내려오면 그 끝에 결론이 나옴
    # child node가 target과 더 가까운지를 판정해서 closest 갱신
