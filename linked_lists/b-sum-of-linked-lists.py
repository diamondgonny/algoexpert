# 문제 풀이 1
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    linkedListList = [linkedListOne, linkedListTwo]
    res = 0

    # 결과값 구함: res (int)
    for node in linkedListList:
        cnt = 0
        while node is not None:
            res += node.value * 10 ** cnt
            node = node.next
            cnt += 1

    # 새로운 linked list로 변환하여 반환
    if res == 0:
        return LinkedList(0)
    else:
        dummy = curr = LinkedList(0)
        while res > 0:
            digit = res % 10
            curr.next = LinkedList(digit)
            curr = curr.next
            res //= 10

    return dummy.next
