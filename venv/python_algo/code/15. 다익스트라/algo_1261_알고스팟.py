# 아르고스~ 알고~~~ 알고리즘~
# 개 필요 없는 존나 맴매 마렵네 이거
# 벽을 몇개 부숴야하냐를 묻는 문젠데 이거 흠 탐색 문제 아닌가
# N,M 이 100개 밖에 안되서 시간 문제도 상관없을꺼고 이게 다익스트라로 풀 수는 있나?
# 우선 BFS 로 풀고 그담에 맞추면 다익스트라로도 풀어보고 그래봅시다 캬 완전 사골이네 사골
# 아아아아아 이게 왜 다익스트라라고 한줄 알겠고 왜 이런 풀이가 된지 알겠네
# 그니까 다익스트라는 사실 bfs 랑 비슷함
# 큐에 넣고 빼고를 하면서 로직을 수행하자나
# 여기서 다익스트라는 한번 진화를 했지 단순히 큐로만 조지면 n^2 을 달려버리니까
# heapq 를 박아서 좀 더 빠른 얘를 뽑도록 했지 그게 현재의 다익스트라야
# 이걸 적용한게 여기 코드의 appendleft 임 벽이 아닌 얘를 가장 앞에 둬서 얘 먼저 계산하라고 밀어주는거지
# 고로 다익스트라와 BFS 는 원리상으로는 상당히 유사하다라고 볼 수 있겠네
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



