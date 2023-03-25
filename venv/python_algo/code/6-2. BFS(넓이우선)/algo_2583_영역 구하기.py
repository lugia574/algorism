import sys
from collections import deque

def BFS(x, y):
    global res
    q.append([x, y])
    check[x][y] = res
    cnt = 1
    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < m and 0 <= ny < n and check[nx][ny] == 0:
                check[nx][ny] = res
                cnt += 1
                q.append([nx,ny])
    return cnt


if __name__ == "__main__":
    input = sys.stdin.readline
    m, n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(k)]
    q = deque()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    check = [[0] * n for _ in range(m)]
    res = 1
    resArr = []
    for c in arr:
        x1, y1, x2, y2 = c
        for i in range(y1, y2):
            for j in range(x1, x2):
                check[i][j] = -1

    for i in range(m):
        for j in range(n):
            if check[i][j] == 0:
                cnt = BFS(i, j)
                resArr.append(cnt)
                res += 1


    resArr.sort()
    print(res-1)
    for i in resArr:
        print(i, end=" ")



