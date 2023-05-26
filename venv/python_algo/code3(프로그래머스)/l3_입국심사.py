# 대체 뭘 기준으로 나눠야하냐
# 심사원을 나눈다는건 말이 안돼 예제는 2명이지만 조건에선 몇명이든 되거든
# 그럼 시간인데 대충 케이스마다 최대 걸리는 시간 심사원 * n 하면 right 값
# 근데 어떻게 해야하나 어떻게  lt, rt 값 갱신을 해주는데

import sys

def solution(n, times):
    times.sort()
    judges = len(times)

    left = 1
    right = times[judges-1] * n

    while left <= right:
        mid = (left + right) // 2
        p = 0
        for i in range(judges): # 난 이게 이해가 안가
            p += mid // times[i]
        if p < n:
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    result = 28
    ans = solution(n, times)
    print(ans)
    print(result == ans)