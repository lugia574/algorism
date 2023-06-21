import sys
from collections import deque

def BFS(a, b):
    q = deque()
    q.append((a, b))
    arr = [(a, b)]
    visited[a][b] = False

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] and board[x][y] == board[nx][ny]:
                visited[nx][ny] = False
                q.append((nx, ny))
                arr.append((nx,ny))

    return arr

def ClearAndDown(arr):
    for x, y in arr:
        board[x][y] = '.'

    for i in range(n-1, -1, -1):
        for j in range(6):
            if board[i][j] != '.':
                x, y = i, j
                tmp = board[x][y]
                while x+1 < 12 and board[x+1][y] == '.':
                    board[x][y] = '.'
                    board[x+1][y] = tmp
                    x += 1


if __name__ == "__main__":
    input = sys.stdin.readline
    board = [list(input().rstrip()) for _ in range(12)]
    n = 12
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    while True:
        visited = [[True] * 6 for _ in range(12)]
        end = True
        clearArr = []
        for i in range(n-1, -1, -1):
            for j in range(6):
                if board[i][j] != '.' and visited[i][j]:
                    blockArr = BFS(i, j)

                    if len(blockArr) > 3:
                        for loc in blockArr:
                            clearArr.append(loc)

        if clearArr:
            ClearAndDown(clearArr)
            cnt += 1
            end = False

        if end:
            break

    print(cnt)



# ......
# ......
# ......
# ......
# ......
# ....Y.
# ....Y.
# ....Y.
# ....RR
# ...YRR
# ..GGYY
# ..GGYY

# answer 2
