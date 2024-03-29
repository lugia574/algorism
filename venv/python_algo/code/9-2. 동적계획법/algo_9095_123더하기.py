# dp[4] = 1111, 121, 112, 211, 31, 13, 22 > 7 > 1 + 2 + 4
# dp[5] = 111/11, 2111, 1211, 1121, 1112, 311, 131, 113, 122, 212, 221, 23, 32 > 13 >  2 + 4 + 7

import sys
if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        if n == 1 or n == 2:
            print(n)
            continue
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for i in range(4, n+1):
            dp[i] = (dp[i-3] + dp[i-2] + dp[i - 1]) % 1000000009
        print(dp[n])

