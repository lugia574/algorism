import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, target = map(int, input().split())
    treeHeight = list(map(int, input().split()))

    lt, rt =1, max(treeHeight)

    ans = 0
    while lt <= rt:
        sumVal = 0
        half = (lt + rt) // 2
        for x in treeHeight:
            if x > half:
                sumVal += x - half

        if sumVal >= target:
            lt = half + 1
        else:
            rt = half - 1


    print(rt)
