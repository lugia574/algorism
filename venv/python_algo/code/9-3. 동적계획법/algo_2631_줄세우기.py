# https://velog.io/@soobin519/Python-백준-2631-줄세우기
# 가장 긴 증가하는 부분수열을 구해서 그 길이를 n에서 빼주면 된다.
# 라는데 이게 뭔소리고?
# 내 추리인데
# 부분 증가 수열이란게 뭐야 https://www.acmicpc.net/problem/11053
# 즉 안만져도 증가 수열이 되는 길이를 구하고
# 그걸 전체에서 빼면 나머지 값은 수정을 해줘 하는 갯수라는 소리지

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    row = [0]
    dp = [1] * (n+1)
    for _ in range(n):
        row.append(int(input()))

    for i in range(1, n + 1):
        for j in range(1, i):
            if row[j] < row[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(n - max(dp))