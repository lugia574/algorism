import sys
from collections import deque

def BFS(a, b):
    while q:
        x, y = q.popleft()
        if x == a and y == b:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (board[nx][ny] == '.' or board[nx][ny] == 'D') and board[x][y] == 'S':
                    board[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                elif (board[nx][ny] == '.' or board[nx][ny] == 'S') and board[x][y] == '*':
                    board[nx][ny] = '*'
                    q.append((nx, ny))

    return "KAKTUS"


if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = [list(map(str, input().strip())) for _ in range(r)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    day = -1
    q = deque()
    targetX = targetY = 0
    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                q.append((i,j))
            elif board[i][j] == 'D':
                targetX, targetY = i, j
    for i in range(r):
        for j in range(c):
            if board[i][j] == '*':
                q.append((i,j))

    answer = BFS(targetX, targetY)
    print(answer)