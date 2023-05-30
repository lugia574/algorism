import sys
from collections import deque

def edgeBFS(v):
    q = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == v:
                dist[i][j] = 0
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 0 and board[nx][ny] != v:
                    # for x in dist:
                    #     print(x)
                    return dist[x][y]
                elif board[nx][ny] != v and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


def islandBFS(a, b):
    global cnt
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    board[nx][ny] = cnt


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().rsplit())) for _ in range(n)]
    cnt = 2
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0] * n for _ in range(n)]
    res = 1e9
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and board[i][j] == 1:
                visited[i][j] = 1
                board[i][j] = cnt
                islandBFS(i, j)
                cnt += 1

    for v in range(2, cnt):
        res = min(res, edgeBFS(v))

    print(res)



# 5
# 1 1 0 0 0
# 1 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 1 1 0 0