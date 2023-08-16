import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [0] * 1001
    startPoint, endPoint = 1001, 0
    topHeight, topHeightIdx = 0, 0

    for _ in range(n):
        idx, h = map(int, input().split())
        arr[idx] = h
        startPoint = min(idx, startPoint)
        endPoint = max(idx, endPoint)

        if topHeight < h:
            topHeightIdx = idx
            topHeight = h

    point = arr[startPoint]
    lt = 0
    for i in range(startPoint, topHeightIdx):
        h = arr[i]
        if point < h:
            point = h
        lt += point

    point = arr[endPoint]
    rt = 0
    for i in range(endPoint, topHeightIdx, -1):
        h = arr[i]
        if point < h:
            point = h
        rt += point


    res = rt + lt + topHeight

    print(res)
