# 여기서 잠깐
# 최장 공통 부분 수열(LCS) == 최장 공통 문자열 이란?
# 두개의 문자서열 x,y 이 주어졌을때
# x,y 에서 공통으로 나타나는 부분 문자열길이가 최대

# https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence



# def lcs(x,y):
#
#     if m == 0 or n == 0:
#         return 0
#     if x[-1] == y[-1]:
#         return lcs(x[:m-1], y[:n-1]) + 1
#     else:
#         return max(lcs(x[:m], y[:n-1]), lcs(x[:m-1], y[:n]))

import sys

def lcs(x,y):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[m][n]

if __name__ == "__main__":
    input = sys.stdin.readline
    x = list(input().strip())
    y = list(input().strip())
    res = lcs(x, y)
    print(res)