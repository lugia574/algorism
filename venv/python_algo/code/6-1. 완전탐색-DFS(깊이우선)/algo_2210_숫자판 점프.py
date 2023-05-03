import sys
sys.setrecursionlimit(10**6)

def DFS(x, y, num, lev):
    if lev == 6:
        ans.add(num)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                DFS(nx, ny, num + board[nx][ny], lev + 1)

if __name__ == "__main__":
    input = sys.stdin.readline
    board = [list(map(str, input().split())) for _ in range(5)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = set()

    for i in range(5):
        for j in range(5):
            DFS(i, j, board[i][j], 1)

    print(len(ans))