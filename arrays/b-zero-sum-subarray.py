# 문제 풀이 1
def zeroSumSubarray(nums):
    c_sum = 0
    map = {0: -1}

    for i, v in enumerate(nums):
        c_sum += v
        if c_sum in map:
            print([val for val in nums[map[c_sum]+1:i+1]])  # subarray
            return True
        map[c_sum] = i

    return False


# Q.
## map[i] = c_sum으로 하는건 좋은 생각이 아니니?

# A.
## 만약 map[인덱스] = 누적합으로 저장한다면 문제가 발생합니다.

## 검색의 비효율성: 현재 c_sum이 해시 맵의 값으로 존재하는지를 찾아야 합니다.
## 해시 맵은 키를 통해 값을 찾는 데 최적화되어 있지, 값을 통해 키를 찾는 데는 적합하지 않습니다.
## 값을 찾으려면 해시 맵의 모든 엔트리를 순회해야 하므로, 검색 시간이 O(N)으로 늘어나게 됩니다.

## 부분 배열 시작 인덱스 확인 불가: 설령 c_sum이 값으로 존재한다는 것을 알아냈다고 해도,
## 해당 c_sum에 대응하는 인덱스(키)를 바로 얻어내기가 어렵습니다. 결국, O(1)의 장점을 잃습니다.

## 따라서, 합이 0인 연속 부분 배열을 O(N)의 평균 시간 복잡도로 찾기 위해서는
## map[누적합] = 인덱스의 구조가 필수적입니다.
