import sys
from itertools import combinations
from collections import deque

def BFS(arr, cnt):
    time = 0
    visited = [[0] * n for _ in range(n)]
    q = deque()
    for vx, vy in arr:
        q.append((vx, vy, 0))
        visited[vx][vy] = 1

    while q:
        x, y, t = q.popleft()
        time = max(t, time)
        if cnt == 0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and board[nx][ny] != 1:
                    q.append((nx, ny, t+1))
                    visited[nx][ny] = visited[x][y] + 1
                    if board[nx][ny] == 0:
                        cnt -= 1

    if cnt > 0:
        time = n*n + 1
    return time

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    v = []
    cnt = 0
    res = n*n + 1

    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                v.append((i, j))
            elif board[i][j] == 0:
                cnt += 1

    vComb = combinations(v, m)

    for vArr in vComb:
        ans = BFS(vArr, cnt)

        res = min(res, ans)

    if res == n*n + 1:
        print(-1)
    else:
        print(res)


    # 5 1
    # 1 1 1 1 1
    # 1 1 1 1 1
    # 1 1 1 1 1
    # 0 2 0 2 0
    # 1 1 1 1 1