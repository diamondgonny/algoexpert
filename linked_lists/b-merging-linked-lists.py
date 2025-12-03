# 문제 풀이 1
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    l1 = linkedListOne
    l2 = linkedListTwo

    while l1 != l2:
        if not l1:
            l1 = linkedListTwo
        else:
            l1 = l1.next
        if not l2:
            l2 = linkedListOne
        else:
            l2 = l2.next

    return l1
