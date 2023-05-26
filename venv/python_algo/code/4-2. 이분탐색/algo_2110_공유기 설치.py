import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, c = map(int, input().rsplit())
    loc = [int(input()) for _ in range(n)]

    loc.sort()
    lt = 1
    rt = loc[-1] - loc[0]

    while lt <= rt:
        mid = (lt + rt) // 2
        curloc = loc[0]
        cnt = 1
        for i in range(1, n):
            if loc[i] > curloc + mid:
                cnt += 1
                curloc = loc[i]
        if cnt >= mid:
            lt = mid + 1
        else:
            rt = mid - 1
    print(lt)