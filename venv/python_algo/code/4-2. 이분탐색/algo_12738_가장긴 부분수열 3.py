# 먼가 개같은데? 왜 바이너리 라이브러리 그런게 잇냐
# 그거 꼴보기 싫어서 딴 방법 찾으니까 DFS ㅇㅈㄹ이네

import sys

def binary(start, end, target):
    if start > end:
        return start
    mid = (start + end) // 2
    if res[mid] > target:
        return binary(start, mid-1, target)

    elif res[mid] == target:
        return mid

    else:
        return binary(mid+1, end, target)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))

    res = [arr[0]]
    for i in range(1, n):
        if res[-1] < arr[i]:
            res.append(arr[i])
        else:
            res[binary(0, len(res)-1, arr[i])] = arr[i]

    print(len(res))


# def dp():
#     dp = [1] * n
#     for i in range(n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[i-1] + 1)
#     print(dp)
#     return
