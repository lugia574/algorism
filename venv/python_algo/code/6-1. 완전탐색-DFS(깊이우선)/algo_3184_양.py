import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    global cntWolf, cntSheep
    if board[x][y] == 'o':
        cntSheep += 1
    elif board[x][y] == 'v':
        cntWolf += 1

    board[x][y] = '#'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] == '#': continue
            DFS(nx, ny)


if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = [list(map(str, input().strip())) for _ in range(r)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False] * c for _ in range(r)]
    sheep = 0
    wolf = 0
    cntWolf, cntSheep = 0, 0

    for i in range(r):
        for j in range(c):
            if board[i][j] == '#': continue
            cntWolf, cntSheep = 0, 0
            DFS(i, j)

            if cntSheep > cntWolf: sheep += cntSheep
            else: wolf += cntWolf



    print(sheep, wolf)