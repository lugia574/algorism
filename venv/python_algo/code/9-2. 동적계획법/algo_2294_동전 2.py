
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    dp = [10001] * (10000 + 1)


    for i in coins:
        for j in range(i, k+1):
            if j - i == 0:
                dp[j] = 1
            elif j - i > 0:
                dp[j] = min(dp[j-i] + 1, dp[j])
        print(dp[:k+1])
    print(dp[k] if dp[k] != 10001 else -1)