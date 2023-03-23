import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    backpack = []

    for _ in range(n):
        backpack.append(list(map(int, input().split())))
    #backpack.sort()
    #print(backpack)
    dp = [[0] * (k+1) for _ in range(n+1)]


    for i in range(n):
        w, v = backpack[i]

        for j in range(1, k + 1):
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

        #print(w, v,dp[i])
    print(max(dp[n-1]))


# 4 7
# 6 13
# 4 8
# 3 6
# 5 12


# 5 7
# 6 13
# 4 8
# 3 6
# 5 12
# 1 20

