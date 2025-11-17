# 문제 풀이 1
def majorityElement(array):
    res = None
    cnt = 0

    for x in array:
        if cnt == 0:
            res = x
            cnt += 1    # 이걸 놓쳐서 좀 헤맴;
        elif res == x:
            cnt += 1
        else:
            cnt -= 1

    return res

# Boyer–Moore Majority Vote Algorithm
# 마치 majority팀과 non-majority팀이 싸워서 majority팀이 승리한다는 내용임
