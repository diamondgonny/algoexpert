# 문제 풀이 1
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    cnt = 0

    node = head
    while node is not None:  # 링크드리스트 길이 정찰 (아래에서 삭제)
        cnt += 1
        node = node.next
    cnt -= k

    node = head
    if cnt == 0:  # head node를 가리킬 때의 base case
        # head = node.next (x)
        node.value = node.next.value
        node.next = node.next.next
    else:
        while cnt > 1:  # 삭제 바로 직전 노드에 도달
            cnt -= 1
            node = node.next
        node.next = node.next.next
