# 문제 풀이 1
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    res = []

    def dfs(node, current_sum):
        if node is None:
            return
        current_sum += node.value
        if node.left is None and node.right is None:
            res.append(current_sum)
            return
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

    dfs(root, 0)
    return res


# 문제 풀이 2
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if root is None:
        return []
    branches = branchSums(root.left) + branchSums(root.right)
    if not branches:
        return [root.value]
    return [x + root.value for x in branches]
