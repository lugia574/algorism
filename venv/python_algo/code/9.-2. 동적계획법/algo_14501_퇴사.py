# (1 ≤ N ≤ 15)
# (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    consulting = []
    for _ in range(n):
        consulting.append(list(map(int,input().split())))

    dp = [0] * 16

    for i in range(n-1, -1, -1):
        day, pay = consulting[i]
        if i + day > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + day] + pay, dp[i + 1])

        print(dp[0])

