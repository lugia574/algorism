import math
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    dp = [math.inf] * (100000+1)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1

    for j in range(6, n+1):
        dp[j] = min(dp[j-2], dp[j-5])+1

    if dp[n] == math.inf:
        dp[n] = -1

    print(dp[n])