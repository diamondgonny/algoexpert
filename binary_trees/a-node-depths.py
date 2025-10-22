# 문제 풀이 1 (top-down)
def nodeDepths(root):
    return dfs(root, 0)

def dfs(node, depth=0):
    if not node:
        return 0
    return depth + dfs(node.left, depth + 1) + dfs(node.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
