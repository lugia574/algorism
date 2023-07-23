# 나 약간 뭔소린지 이해가 안가

import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    q = deque()
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append((i, j))

    dx = [-1, -1, -1, 0, 1, 0, 1, 1]
    dy = [-1, 0, 1, 1, 1, -1, 0, -1]

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx > n-1 or 0 > ny or ny > m-1:
                continue
            if board[nx][ny] != 0:
                continue
            q.append((nx, ny))
            board[nx][ny] += board[x][y] + 1
            answer = max(board[nx][ny], answer)

    print(answer-1)