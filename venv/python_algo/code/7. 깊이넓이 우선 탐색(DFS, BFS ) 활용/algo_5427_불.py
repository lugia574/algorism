# 이렇게 하니까 시초 걸림

import sys
from collections import deque

def BFS(me, f):
    q = deque()
    for fx, fy in f:
        q.append((fx, fy, board[fx][fy]))

    q.append((me[0], me[1], board[me[0]][me[1]]))
    while q:
        x, y, s = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if board[nx][ny] != '#' and board[nx][ny] != '*':

                    if s == '@' and visited[nx][ny] == 0:
                        visited[nx][ny] += visited[x][y] + 1
                        if nx == 0 or nx == h+1 or ny == 0 or ny == w+1:
                            return visited[nx][ny]

                    board[nx][ny] = s
                    q.append((nx, ny, s))
    return 0

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        w, h = map(int, input().rsplit())
        tmp = [list(map(str, input().rstrip())) for _ in range(h)]

        board = [['.'] * (w+2) for _ in range(h+2)]
        fire = []
        start = []

        visited = [[0] * (w+2) for _ in range(h+2)]
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

        for i in range(h):
            for j in range(w):
                board[i+1][j+1] = tmp[i][j]

                if tmp[i][j] == '@':
                    start = (i+1, j+1)
                elif tmp[i][j] == '*':
                    fire.append((i+1, j+1))

        ans = BFS(start, fire)

        print("IMPOSSIBLE" if ans == 0 else ans)

# 1
# 4 3
# ####
# #*@.
# ####

# 1
# 7 6
# ###.###
# #*#.#*#
# #.....#
# #.....#
# #..@..#
# #######