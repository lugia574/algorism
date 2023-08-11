import sys
from collections import deque

def bfs(a, b):
    global blueScore, whiteScore
    q = deque()
    q.append((a, b))
    teamCounter = 1
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= m or 0 > ny or ny >= n or visited[nx][ny] or board[nx][ny] != board[x][y]:
                continue
            visited[nx][ny] = True
            teamCounter += 1
            q.append((nx, ny))

    if board[a][b] == 'W':
        whiteScore += (teamCounter ** 2)
    else:
        blueScore += (teamCounter ** 2)



if __name__ == "__main__":
    input = sys.stdin.readline
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    n, m = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    blueScore = 0
    whiteScore = 0

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)

    print(whiteScore, blueScore)