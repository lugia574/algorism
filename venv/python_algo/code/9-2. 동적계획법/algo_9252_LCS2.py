import sys

def lcs(x,y):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0

    dp = [[""] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + x[i-1]
            else:
                if len(dp[i][j - 1]) < len(dp[i - 1][j]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]


    return len(dp[m][n]), dp[m][n]

if __name__ == "__main__":
    input = sys.stdin.readline
    x = list(input().strip())
    y = list(input().strip())
    cnt, res = lcs(x, y)
    print(cnt)
    print(res)