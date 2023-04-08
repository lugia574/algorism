# 솔직히 말해서 잘 이해 안가오

import sys, math

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        files = list(map(int, input().split()))
        dp = [[0] * n for _ in range(n)]

        for j in range(1, n):
            for i in range(j-1, -1, -1):
                small = math.inf
                for k in range(j-i):
                    small = min(small, dp[i][i + k] + dp[i + k + 1][j])
                dp[i][j] = small + sum(files[i:j+1])

        print(dp[0][n-1])





# 1
# 4
# 40 30 30 50
