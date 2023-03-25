# 1. 아이디어
# BFS 로 풀고 감염될때마다 값을 늘려서 배열에 박아주고 가장 큰 값을 뽑으면 될듯?
# 근데 해당 배열에 0 이 있으면 -1 을 뽑아내게 하면 될듯?
# 참고로 익은 토마토들을 먼저 q 에 박고 나서 그 다음에 BFS 를 돌려야함

import sys
from collections import deque

def BFS():
    global q
    DAY = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= yy < n and 0 <= xx < m and tomato[yy][xx] == 0:
                tomato[yy][xx] = tomato[y][x] + DAY
                q.append((yy, xx))


if __name__ == "__main__":
    input = sys.stdin.readline
    m, n = map(int, input().split())
    tomato = [list(map(int, input().split())) for _ in range(n)]
    q = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = 0
    # for i in tomato:
    #     print(i)

    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                q.append((i, j))
    BFS()

    for row in tomato:
        if 0 in row:
            res = -1
            break
        else:
            res = max(max(row),res)

    print(res - 1 if res != -1 else res)

