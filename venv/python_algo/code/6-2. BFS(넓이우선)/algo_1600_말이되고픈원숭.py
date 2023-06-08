# 이게 나는 그냥 말 점프만 따로 count 해주면 될꺼라고 생각했는데
# 그러면 visited 부분에서 꼬이게 됨
# 그렇기에 말이 점프를 했냐 안했냐를 z 로 나눠서
# 3차원 visited를 해야해함
# 코드에는 31 까지 확장 해버리는데
# 그냥 k 까지만 초기화 해줘도 됨

import sys
from collections import deque


def BFS():
    q = deque()
    q.append((0, 0, k))
    visit = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]
    while q:
        x, y, z = q.popleft()
        if x == h - 1 and y == w - 1: return visit[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != 1 and visit[nx][ny][z] == 0:
                visit[nx][ny][z] = visit[x][y][z] + 1
                q.append((nx, ny, z))
        if z > 0:
            for i in range(8):
                nx = x + d1[i]
                ny = y + d2[i]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != 1 and visit[nx][ny][z - 1] == 0:
                    visit[nx][ny][z - 1] = visit[x][y][z] + 1
                    q.append((nx, ny, z - 1))
    return -1

if __name__ == "__main__":
    input =sys.stdin.readline
    k = int(input())
    w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    d1 = [-2, -1, 1, 2, 2, 1, -1, -2]
    d2 = [1, 2, 2, 1, -1, -2, -2, -1]

    res = BFS()
    print(res)


    # 2
    # 10 2
    # 0 0 1 0 0 1 0 0 1 0
    # 0 0 1 1 0 0 0 0 1 0