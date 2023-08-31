# 아르고스~ 알고~~~ 알고리즘~
# 개 필요 없는 존나 맴매 마렵네 이거
# 벽을 몇개 부숴야하냐를 묻는 문젠데 이거 흠 탐색 문제 아닌가
# N,M 이 100개 밖에 안되서 시간 문제도 상관없을꺼고 이게 다익스트라로 풀 수는 있나?
# 우선 BFS 로 풀고 그담에 맞추면 다익스트라로도 풀어보고 그래봅시다 캬 완전 사골이네 사골

import sys
from collections import deque

def BFS():
    global res

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 > nx or nx >= n or 0 > ny or ny >= m or dist[nx][ny] != -1: continue

            if board[nx][ny] == '1':
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
            else:
                q.appendleft((nx, ny))
                dist[nx][ny] = dist[x][y]

if __name__ == "__main__":
    input = sys.stdin.readline
    m, n = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dist = [[-1] * (m) for _ in range(n)]
    dist[0][0] = 0

    BFS()
    print(dist[n-1][m-1])



