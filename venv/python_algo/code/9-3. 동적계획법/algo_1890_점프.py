import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] > 0 and board[i-1][j-1] != 0:
                jump = board[i-1][j-1]
                if i + jump <= n:
                    dp[i + jump][j] += dp[i][j]
                if j + jump <= n:
                    dp[i][j+jump] += dp[i][j]
    print(dp[n][n])