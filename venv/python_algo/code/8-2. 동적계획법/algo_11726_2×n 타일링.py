import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    dp = [0] * (1000+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 10007

    print(dp[n])