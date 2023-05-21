import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    schedule = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n+1)

    for i in range(n - 1, -1, -1):
        day, pay = schedule[i]
        if i + day > n:
            # dp[i] = dp[i + 1]
            continue
        else:
            dp[i] = max(dp[i + day] + pay, dp[i + 1])
    # print(dp)
    print(dp[0])