# 문제 풀이 1
from collections import Counter
def firstNonRepeatingCharacter(string):
    cntr = Counter(string)
    for i, c in enumerate(string):
        if cntr[c] == 1:
            return i
    return -1
