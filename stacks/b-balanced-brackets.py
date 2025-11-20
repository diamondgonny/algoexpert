# 문제 풀이 1
def balancedBrackets(string):
    brkStart = "([{"
    brkEnd = ")]}"
    brkMatch = {")":"(", "]":"[", "}":"{"}
    stack = []

    for c in string:
        if c in brkStart:
            stack.append(c)
        if c in brkEnd:
            if not stack:
                return False
            elif stack[-1] == brkMatch[c]:
                stack.pop()
            else:
                return False

    return True if not len(stack) else False


# 문제 풀이 1'
def balancedBrackets(string):
    pairs = {")":"(", "]":"[", "}":"{"}
    stack = []

    for c in string:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs:
            if not stack:
                return False
            elif stack.pop() != pairs[c]:
                return False

    return not stack
