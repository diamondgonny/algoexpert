# 문제 풀이 1
def runLengthEncoding(string):
    new_string = ""
    a = ''
    n = ''
    for c in string:
        if c != a or n == 9:
            new_string += str(n)
            new_string += a
            a = c
            n = 1
        else:
            n += 1
    new_string += str(n)
    new_string += a
    return new_string

# 문제 풀이 2 (/w 복기)
def runLengthEncoding(string):
    ret, cnt = "", 1

    for i in range(1, len(string)):
        if string[i] != string[i - 1] or cnt == 9:
            ret += f"{str(cnt)}{string[i - 1]}"
            cnt = 1
        else:
            cnt += 1

    ret += f"{str(cnt)}{string[len(string) - 1]}"
    return ret

# 두 풀이의 차이:
# 1) 변수 a를 빼고, string 내의 문자를 직접 비교함
# 2) 반복문 범위 사용
# 3) f-string 사용
# 4) 두 줄로 쓰던 걸 한 줄로 통합
