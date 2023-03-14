import sys
from collections import deque

def BFS(y, x, z):
    q = deque()
    q.append((y, x, z))
    while q:
        y, x, z = q.popleft()
        if y == n-1 and x == m-1:
            return check[y][x][z]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 0 and check[ny][nx][z] == 0:
                    check[ny][nx][z] = check[y][x][z] + 1
                    q.append((ny, nx, z))
                elif map[ny][nx] == 1 and z == 0:
                    check[ny][nx][1] = check[y][x][0] + 1
                    q.append((ny, nx, 1))

    return -1

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    map = [list(map(int, input().strip())) for _ in range(n)]
    check = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    check[0][0][0] = 1
    res = BFS(0,0,0)

    print(res)