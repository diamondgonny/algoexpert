# 문제 풀이 1
def bestDigits(number, numDigits):
    stack = []

    for digit in number:
        while stack and stack[-1] < digit and numDigits:
            stack.pop()
            numDigits -= 1
        stack.append(digit)

    if numDigits:
        stack = stack[:-numDigits]

    return "".join(stack)
