import sys
from collections import deque
# l(4 ≤ l ≤ 300)

def BFS(loc):
    q.append(loc)
    board[loc[0]][loc[1]] = 1

    while q:
        y, x = q.popleft()
        if y == end[0] and x == end[1]:
            print(board[end[0]][end[1]]-1)
            break

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < l and 0 <= nx < l and board[ny][nx] == 0:
                q.append((ny, nx))
                board[ny][nx] = board[y][x] + 1

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    for _ in range(T):
        q = deque()
        l = int(input())
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))

        board = [[0] * l for _ in range(l)]
        BFS((start[0],start[1]))



