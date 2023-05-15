# 행렬 곱셉에 대해서 알아둬야할듯?
# 행렬곱셉 개념: https://www.youtube.com/watch?v=qwEWO-cQwXQ
# (m, k) * (k, n) = (m, n) 열이 됨
# 이게 문제가 뭐냐면 단순히 n 이 3개면 그냥 dp로 할것도 없어
# min 함수 쳐서 바로 할 수 있단 말이야
# 근데 최대 500까지 나오는데 곱이 되는 행렬 있고, 안되는 행렬이 있을꺼 아녀
# 못해도 2차 배열 dp 로 해야할꺼 같은데
# https://claude-u.tistory.com/271

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(0, n-i):
            if i == 1:  # 차이가 1밖에 나지 않는 칸
                dp[j][j + i] = matrix[j][0] * matrix[j][1] * matrix[j + i][1]
                continue

            dp[j][j + i] = 2 ** 32  # 최댓값을 미리 넣어줌
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i],
                                   dp[j][k] + dp[k + 1][j + i] + matrix[j][0] * matrix[k][1] * matrix[j + i][1])

    print(dp[0][n - 1])  # 맨 오른쪽 위