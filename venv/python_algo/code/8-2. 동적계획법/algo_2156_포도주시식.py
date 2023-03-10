
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    wine = []
    dp = [0] * (n+1)
    for _ in range(n):
        wine.append(int((input())))
    if n == 1 :
        print(wine[0])
        sys.exit()

    dp[1] = wine[0]
    dp[2] = dp[1] + wine[1]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + wine[i-2] + wine[i-1], dp[i-2] + wine[i-1], dp[i-1])


    print(max(dp))