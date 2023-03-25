import sys
from collections import deque

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
input = sys.stdin.readline

def BFS(y, x):
    q.append((y, x))
    while q:
        y, x = q.popleft()
        island[y][x] = 0
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and island[ny][nx] == 1:
                q.append((ny, nx))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    island = [list(map(int, input().split())) for _ in range(h)]
    landCnt = 0
    q = deque()

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                BFS(i, j)
                landCnt += 1
    print(landCnt)



