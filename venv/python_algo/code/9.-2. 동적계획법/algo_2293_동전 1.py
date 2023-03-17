#  (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, k = map(int, input().split())
    coin = []
    for _ in range(n):
        coin.append(int(input()))
    dp = [0] * (k+1)

    dp[0] = 1
    for i in coin:
        for j in range(1, k+1):
            if j - i >= 0:
                dp[j] += dp[j-i]
        #print(dp)
    print(dp[k])
