import sys
sys.setrecursionlimit(int(1e9))

def dfs(x, y):
    if y == c-1:
        return True
    for dx in [-1, 0, 1]:
        nx = x + dx
        ny = y + 1
        if 0 > nx or nx >= r or y >= c or board[nx][ny] == 'x' or visited[nx][ny] == 1:
            continue
        visited[nx][ny] = 1
        if dfs(nx, ny):
            return True
    return False


if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(r)]
    visited = [[0] * c for _ in range(r)]
    move = ((0, 1), (1, 1), (-1, 1))
    answer = 0
    for i in range(r):
        if dfs(i, 0): answer += 1

    print(answer)