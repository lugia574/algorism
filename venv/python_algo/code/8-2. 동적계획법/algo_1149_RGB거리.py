import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    house = [list(map(int, input().split())) for _ in range(n)]

    dp = [0] * (n+1)

    # for i in range(n):
    #     dp[i] = min()