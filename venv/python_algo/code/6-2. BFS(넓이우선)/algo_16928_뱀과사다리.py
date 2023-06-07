# 이건 사실상 보고 한거임
# 크게 어려운건 없었는데 딕셔너리를 쓰는 걸 내가 좀 생소했음
import sys
from collections import deque

def BFS():
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        x = q.popleft()
        for jump in range(1, 7):
            nx = x + jump
            if -1 < nx < 101 and not visited[nx]:
                if nx in ladder.keys():
                    nx = ladder[nx]
                if nx in snack.keys():
                    nx = snack[nx]

                if not visited[nx]:
                    visited[nx] = True
                    q.append(nx)
                    board[nx] = board[x] + 1



if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [0] * 101
    visited = [False] * 101
    ladder = dict()
    snack = dict()
    for _ in range(n):
        a, b = map(int, input().split())
        ladder[a] = b
    for _ in range(m):
        a, b = map(int, input().split())
        snack[a] = b

    BFS()
    print(board[100])