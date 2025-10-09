# 문제 풀이 1
def semordnilap(words):
    res = []
    for i, s in enumerate(words):
        for j in range(i + 1, len(words)):
            if s[::-1] == words[j]:
                res.append([s, s[::-1]])
    return res

# palindrome: s[::-1]
# O(n * m) time: double loop is ok
