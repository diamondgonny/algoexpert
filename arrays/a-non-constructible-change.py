# 문제 풀이 1
def nonConstructibleChange(coins):
    coins = sorted(coins)
    target = 1

    for coin in coins:
        if target < coin:
            return target
        target += coin

    return target
