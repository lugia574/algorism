import sys
from collections import deque

def BFS(a, b):
    q = deque()
    q.append((a, b))
    maxVal = 0
    while q:
        x, y = q.popleft()
        maxVal = max(maxVal, visited[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and board[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return maxVal

if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = [list(map(str, input().strip())) for _ in range(r)]
    dx = [1, 0 , -1, 0]
    dy = [0, 1, 0, -1]
    res = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'L':
                visited = [[0] * c for _ in range(r)]
                visited[i][j] = 1
                returnVal = BFS(i,j)
                res = max(res, returnVal)
    print(res-1)


