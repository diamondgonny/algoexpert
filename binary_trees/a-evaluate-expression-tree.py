# 문제 풀이 1 (bottom-up)
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree.value == -1:
        branches = evaluateExpressionTree(tree.left) + evaluateExpressionTree(tree.right)
    elif tree.value == -2:
        branches = evaluateExpressionTree(tree.left) - evaluateExpressionTree(tree.right)
    elif tree.value == -3:
        branches = int(evaluateExpressionTree(tree.left) / evaluateExpressionTree(tree.right))
    elif tree.value == -4:
        branches = evaluateExpressionTree(tree.left) * evaluateExpressionTree(tree.right)
    else:
        return tree.value
    return branches


# 문제 풀이 2 (bottom-up)
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    ops = {
        -1: lambda l, r: l + r,
        -2: lambda l, r: l - r,
        -3: lambda l, r: int(l / r),
        -4: lambda l, r: l * r
    }
    if tree.value in ops:
        return ops[tree.value](evaluateExpressionTree(tree.left), evaluateExpressionTree(tree.right))
    return tree.value
