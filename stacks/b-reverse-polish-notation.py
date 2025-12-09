# 문제 풀이 1
def reversePolishNotation(tokens):
    stack = []

    for t in tokens:
        if t not in ["+", "-", "*", "/"]:
            stack.append(int(t))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            res = calc(n1, n2, t)  # 이 값을 stack에 넣고 질서있게(?) 해결하기
            stack.append(res)

    return stack[0]

def calc(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return int(a / b)
