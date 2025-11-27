# 문제 풀이 1
# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev:  # node.prev가 NoneType이면 에러가 난답니다...
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

        if node == self.head:
            self.head = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next:  # node.next가 NoneType이면 에러가 난답니다...
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

        if node == self.tail:
            self.tail = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:  # base case
            self.setHead(nodeToInsert)
            return
        node = self.head
        for i in range(position - 1):
            node = node.next
        self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:  # node.value를 비교하고 앉았는...;
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:  # self.head 존재 체크를 하고 앉았는...;
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:  # node.prev가 NoneType이면 에러가 난답니다...
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = node.next = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False
