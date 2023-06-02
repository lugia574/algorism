import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    arr = [list(map(int, input().rsplit())) for _ in range(N)]
    arr = sorted(arr, key = lambda x: (x[1], x[0]))

    dp = [0]
    for i in range(N):
        if arr[i][0] >= dp[-1]:
            dp.append(arr[i][1])
    print(len(dp) - 1)
