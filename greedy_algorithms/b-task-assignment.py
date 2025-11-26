# 문제 풀이 1
def taskAssignment(k, tasks):
    res = []
    tasks_l = [[i, v] for i, v in enumerate(tasks)]
    sorted_tasks_l = sorted(tasks_l, key=lambda x: x[1])  # 난 이게 아직 적응이 안돼...

    for i in range(k):
        res.append([sorted_tasks_l[i][0], sorted_tasks_l[2 * k - 1 - i][0]])

    return res
