# (1 ≤ N ≤ 1,000)

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    card = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        cost = card[i-1]
        for j in range(1, n+1):
            if j % i == 0:
                dp[i][j] = max(dp[i-1][j], (j // i) * cost)
            else:
                if j < i:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i][j-i] + cost, dp[i-1][j])


    print(dp[n][n])

# 1 2 3 4
# 0 0 0 0
# 1 2 3 4 > 1
# 1 5 6 10 > 1,2
# 1 5 7 10 > 1,2,3
# 1 5 7 10 > 1, 2, 3, 4