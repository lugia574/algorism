import sys
from collections import deque

def BFS(a, b):
    q = deque()
    q.append((a, b))
    foodSize = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] == '#':
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    foodSize += 1
    return foodSize

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int,input().rsplit())
    board = [['.'] * m for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0] * m for _ in range(n)]
    maxSize = 0
    for _ in range(k):
        x, y = map(int, input().rsplit())
        board[x-1][y-1] = '#'

    for i in range(n):
        for j in range(m):
            if board[i][j] == '#' and visited[i][j] == 0:
                visited[i][j] = 1
                ans = BFS(i, j)
                maxSize = max(ans, maxSize)

    print(maxSize)