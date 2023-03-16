import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    if n == 1 or n == 2:
        print(1)
        sys.exit()
    elif n == 0:
        print(0)
        sys.exit()

    dp = [0] * (90 + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])