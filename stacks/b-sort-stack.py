# 문제 풀이 1
def sortStack(stack):
    if not stack:
        return []

    top = stack.pop()
    sortStack(stack)
    sortedInsert(stack, top)

    return stack

def sortedInsert(stack, x):
    if not stack or stack[-1] <= x:
        stack.append(x)
        return

    top = stack.pop()
    sortedInsert(stack, x)
    stack.append(top)  # x가 아니라 top을 넣어야, x를 insert하고 뚜껑(top)을 닫음
