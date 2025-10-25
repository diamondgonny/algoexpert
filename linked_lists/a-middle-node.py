# 문제 풀이 1
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    x1 = x2 = linkedList
    while x2 is not None and x2.next is not None:
        x1, x2 = x1.next, x2.next.next
    return x1

    # two pointer
