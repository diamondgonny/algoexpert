# 문제 풀이 1
def optimalFreelancing(jobs):
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    slot = [0, 0, 0, 0, 0, 0, 0]

    for job in jobs:
        dl = min(job["deadline"] - 1, 6)
        for i in range(dl, -1, -1):
            if slot[i] == 0:
                slot[i] = job["payment"]
                break

    return sum(slot)
