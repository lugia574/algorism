import math
import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    p = list(map(int, input().rstrip().split()))

    # dp[i] : i개의 카드를 구매하는데 드는 최소 비용
    dp = [math.inf] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(1, i+1):  # j: 구매하는 카드팩에 들어있는 카드의 개수
            dp[i] = min(dp[i], dp[i-j] + p[j-1])

    #print(dp)
    print(dp[n])