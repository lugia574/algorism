# 대충 sort 해서 
# 투포인터로 갈기면 되지 않을까

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    start = 0
    end = 0
    minVal = sys.maxsize

    while start <= end and end < n:
        gap = arr[end] - arr[start]
        if gap < m:
            end += 1
        else:
            minVal = min(minVal, gap)
            start += 1

    print(minVal)




