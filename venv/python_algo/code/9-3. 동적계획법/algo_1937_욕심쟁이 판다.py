import sys
sys.setrecursionlimit(10 ** 6)
def DFS(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[x][y] < board[nx][ny]:
            dp[x][y] = max(dp[x][y], DFS(nx, ny) + 1)
    return dp[x][y]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    res = 0
    for i in range(n):
        for j in range(n):
            res = max(res, DFS(i, j))
    print(res)