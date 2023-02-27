# 인접행렬(가중치 방향그래프)
# ▣ 입력설명
# 첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연
# 결정보와 거리비용이 주어진다.
# ▣ 출력설명
# 인접행렬을 출력하세요.
# ▣ 입력예제 1
# 6 9
# 1 2 7
# 1 3 4
# 2 1 2
# 2 3 5
# 2 5 5
# 3 4 5
# 4 2 2
# 4 5 5
# 6 4 5
# ▣ 출력예제 1
# 0 7 4 0 0 0
# 2 0 5 0 5 0
# 0 0 0 5 0 0
# 0 2 0 0 5 0
# 0 0 0 0 0 0
# 0 0 0 5 0 0

if __name__ == "__main__":
    n, m = map(int,input().split())

    g = [[0] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        r, c, w = map(int,input().split())
        g[r][c] = w

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(g[i][j], end=" ")
        print()