# 1 > 1^
# 2 > 1^ 1^
# 3 > 1^ 1^ 1^
# 4 > 2^
# 5 > 2^ 1^
# 6 > 2^ 1^ 1^
# 7 > 2^ 1^ 1^ 1^
# 8 > 2^ 2^
# 9 > 3^
# 10 > 3^ 1
# 11 > 3^ 1^ 1^
# 12 > 2^ 2^ 2^
import math, sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        num = i ** 0.5
        minValue = math.inf
        if num == int(num):
            dp[i] = 1
        else:
            for j in range(1, int(num) + 1):
                minValue = min(minValue, dp[i - j**2])
            dp[i] = minValue + 1

    print(dp[n])