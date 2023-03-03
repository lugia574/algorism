
import copy
import sys
from collections import deque

def BFS():
    global res
    q = deque()
    cnt = 0
    tmpArr = copy.deepcopy(lab)

    for i in range(n):
        for j in range(m):
            if tmpArr[i][j] == 2:
                q.append((i, j))

    while q:
        y, x = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= yy < n and 0 <= xx < m:
                if tmpArr[yy][xx] == 0:
                    tmpArr[yy][xx] = 2
                    q.append((yy, xx))

    for i in range(n):
        for j in range(m):
            if tmpArr[i][j] == 0:
                cnt += 1
    res = max(res, cnt)


def Wall(cnt):
    if cnt == 3:
        BFS()
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                Wall(cnt+1)
                lab[i][j] = 0

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    res = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    Wall(0)
    print(res)


# 3 6
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2
