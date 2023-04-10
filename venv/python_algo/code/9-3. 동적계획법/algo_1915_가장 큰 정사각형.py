# 이게 왜 이렇게 되냐면
# 나는 원래 이것을 뭐 BFS 로 해서 어떻게 해야하나? 이렇게 생각 했는데
# BFS 로 굴리면 대충 (1000 * 1000)^2 넘을 판이라 안될꺼 같음
# 정사각형만 딱 때는 코드까지 더하면 더 넘겠지? 막막함
# 그래서 dp 를 쓰는 건데
# 우측좌하단 맨 끝을 보고 판단하면 됨
# 이에 대한 설명은 https://kyun2da.github.io/2021/04/09/biggestSquare/ 여길 보면 됨
# 그래서 (i-1, j-1), (i-1, j), (i, j-1) 이 셋 중에 가장 낮은 값 + 1을 해야 정사각형 판별이 가능함
# 정사각형이면 위 값이 전부 같을테니 그대로 값을 챙길것이고 저 셋중에 하나라도 비어 있음 값이 다를 테니 정사각형이 아니게 되는거지
# 정사각형이 아닌데 단순 1로 채워진 값은 그대로 1만 집어 넣어진채로 진행 되는거임

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = arr[i][j]
            elif arr[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            answer = max(dp[i][j], answer)

    print(answer * answer)