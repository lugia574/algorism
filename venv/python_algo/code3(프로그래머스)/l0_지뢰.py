from collections import deque
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def solution(board):
    n = len(board)

    answer = n * n
    visited = [[0] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and board[i][j] == 1:
                answer -= 1
                visited[i][j] = 1
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx, ny)
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 1: continue
                visited[nx][ny] = 1
                answer -= 1

    return answer

if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    res = 16
    answer = solution(board)
    print(res == answer, answer)