# 이거 딱 봐도 부분증가수열 구하고 n - 부분증가수열cnt 해주면 되는거 아님?
# 범위가 1 ≤ N ≤ 100,000 이라 n^2 하면 시초임
# 그러니까 이분탐색으로 풀어야함

import sys

def binary(x):
    start = 0
    end = len(res) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if res[mid] == x:
            return mid
        elif res[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))

    res = [arr[0]]

    for i in range(1, n):
        if res[-1] < arr[i]:
            res.append(arr[i])
        else:
            index = binary(arr[i])
            res[index] = arr[i]

    print(n - len(res))
