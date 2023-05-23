# https://hongcoding.tistory.com/69
# 먼가 이상혀~
# 잘 모르것어~
# 아 물린다 알고리즘 물려 시벌
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(board):
    n = len(board)
    price = [[int(1e9)] * n for _ in range(n)]
    price[0][0] = 0

    queue = deque()
    queue.append((0, 0, 0, 5))  # (시작X, 시작Y, 시작Cost, 시작방향)

    while queue:
        x, y, c, z = queue.popleft()

        if x == n - 1 and y == n - 1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = i

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue

            if z == 5:
                nc = c + 100

            elif nz == z:
                nc = c + 100

            else:
                nc = c + 600

            if nc <= price[nx][ny]:
                price[nx][ny] = nc
                queue.append((nx, ny, nc, i))

    return price[-1][-1]


def solution(board):
    n = len(board)
    answer = bfs(board)
    return answer

if __name__ == "__main__":
    board = [[0,0,0],[0,0,0],[0,0,0]]
    res = 900
    ans = solution(board)
    print(res == ans)

    board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
    res = 3800
    ans = solution(board)
    print(res == ans)

    board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
    res = 2100
    ans = solution(board)
    print(res == ans)

    board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    res = 3200
    ans = solution(board)
    print(res == ans)

    board = [[0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 1, 1, 1, 1, 1, 0],[1, 0, 0, 1, 0, 0, 0, 0],[1, 1, 0, 0, 0, 1, 1, 1],[1, 1, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 0],]
    res = 4500
    ans = solution(board)
    print(ans) # 4900 이면 잘못된거
    print(res == ans)
