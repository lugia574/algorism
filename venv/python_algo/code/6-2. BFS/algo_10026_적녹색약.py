import sys
from collections import deque


def BFS(y, x):
    q = deque()
    q.append((y, x))
    target = picture[y][x]
    while q:
        y, x = q.popleft()
        check[y][x] = True
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < n and picture[yy][xx] == target and not check[yy][xx]:
                q.append((yy, xx))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    picture = [list(map(str, input().strip())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    check = [[False]*n for _ in range(n)]
    area = 0
    rgArea = 0

    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                BFS(i, j)
                area += 1
            if picture[i][j] == "R":
                picture[i][j] = "G"

    check = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                BFS(i, j)
                rgArea += 1


    print(area, rgArea)
    # for i in picture:
    #     print(i)



# def RGBFS(y, x):
#     q = deque()
#     q.append((y, x))
#     target = "X" if picture[y][x] == "R" or picture[y][x] == "G" else picture[y][x]
#     while q:
#         y, x = q.popleft()
#         rgCheck[y][x] = True
#         for i in range(4):
#             yy = y + dy[i]
#             xx = x + dx[i]
#             if 0 <= yy < n and 0 <= xx < n :
#                 target2 = "X" if picture[yy][xx] == "R" or picture[yy][xx] == "G" else picture[yy][xx]
#                 if target2 == target and not rgCheck[yy][xx]:
#                     q.append((yy, xx))