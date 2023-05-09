# https://bio-info.tistory.com/214
# 솔직히 제대로 이해를 못함

import math
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    color = [list(map(int, input().split())) for _ in range(n)]
    ans = math.inf
    for i in range(3):
        dp = [[math.inf] * 3 for _ in range(n)]
        dp[0][i] = color[0][i]
        for j in range(1, n):
            dp[j][0] = color[j][0] + min(dp[j-1][1], dp[j-1][2])
            dp[j][1] = color[j][1] + min(dp[j-1][0], dp[j-1][2])
            dp[j][2] = color[j][2] + min(dp[j-1][0], dp[j-1][1])
        for c in range(3):
            if i != c:
                ans = min(ans, dp[n-1][c])
    print(ans)

# 3
# 1 100 100
# 100 1 100
# 1 100 100