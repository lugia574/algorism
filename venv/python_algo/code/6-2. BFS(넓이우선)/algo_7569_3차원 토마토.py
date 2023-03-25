import sys
from collections import deque

def BFS():
    DAY = 1
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            nz = z + dz[i]
            if 0 <= ny < n and 0 <= nx < m and 0 <= nz < h and tomatoApart[nz][ny][nx] == 0 :
                tomatoApart[nz][ny][nx] = tomatoApart[z][y][x] + DAY
                q.append((nz, ny, nx))


if __name__ == "__main__":
    input = sys.stdin.readline
    m, n, h = map(int, input().split())
    tomatoApart = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    q = deque()
    dx = [0, 0, 1, 0, -1, 0]
    dy = [0, 0, 0, 1, 0, -1]
    dz = [1, -1, 0, 0, 0, 0]
    res = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatoApart[i][j][k] == 1:
                    q.append((i, j, k))

    BFS()
    for floor in tomatoApart:
        for check in floor:
            if 0 in check:
                res = -1
                break
            else:
                res = max(max(check), res)
        if res == -1:
            break


    print(res-1 if res > 0 else res)

# 5 4 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0