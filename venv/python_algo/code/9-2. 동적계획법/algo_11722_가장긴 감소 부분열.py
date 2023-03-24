import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

    # 10 30 10 20 20 10
    # 1  1   2  2  2  3