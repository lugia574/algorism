# 캬이 이거 전에 풀었던 그 뭐냐 그 수 계산 문제랑 같자너 ㅋㅋ
# dp 이차원으로 만들고 n * m 으로 해서
# 처음 시작 점인 dp[0][s] 부터 시작해서 v[i] 값이 0 <= sp <= m 이냐 따져서 쭉 돌리는거지 히이히잉히히히
import sys

def guitarList(n, s, m, v):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][s] = 1
    for i in range(1, n + 1):
        for j in range(0, m + 1):
            if dp[i - 1][j] != 0:
                plusV = j + v[i - 1]
                minusV = j - v[i - 1]
                if 0 <= plusV <= m: dp[i][plusV] = 1 + dp[i - 1][j]
                if 0 <= minusV <= m: dp[i][minusV] = 1 + dp[i - 1][j]

    for x in range(m, -1, -1):
        if dp[n][x] > 0:
            return x

    return -1


if __name__ == "__main__":
    input = sys.stdin.readline
    n, s, m = map(int, input().split())
    v = list(map(int, input().split()))
    res = guitarList(n, s, m, v)
    print(res)