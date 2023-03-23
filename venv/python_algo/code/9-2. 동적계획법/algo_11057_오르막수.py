import sys

def solution():
    n = int(input())
    dp = [1] * 10
    for i in range(1, n):
        for j in range(1, 10):
            dp[j] += dp[j - 1]

    print(sum(dp) % 10007)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    dp = [[0] * 10 for _ in range(n+1)]
    for i in range(10):
        dp[1][i] = 1

    for i in range(2, n+1):
        for j in range(10):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(sum(dp[n]) % 10007)