# n = 1 >> 1
# n = 2 >> 3
# n = 3 >> 000
#          000
#          000
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = [[0] * n for _ in range(3)]
    dp = [0] * (30 + 1)
    dp[1] = 0
    dp[2] = 3
    for i in range(3, 31):
        if i % 2 == 0:
            dp[i] = (dp[i - 2] * dp[2]) +sum(dp[:i-2]) * 2 + 2
        else:
            dp[i] = 0


    print(dp[n])