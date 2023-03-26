# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치
# 가장 처음에 아기 상어의 크기는 2
# 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
# 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
# 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
# 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 뭐라고 하는건지 모르겠는데 아참 ㅇ참
# https://great-park.tistory.com/26

import sys
from collections import deque

def bfs(sharkX, sharkY):
    q = deque()
    q.append((sharkX, sharkY, 0))
    dist = []
    visted = [[0] * n for _ in range(n)]
    visted[sharkX][sharkY] = 1
    minDist = 10000000
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visted[nx][ny] == 0:
                if board[nx][ny] <= sharkSize:
                    visted[nx][ny] = 1
                    if 0 < board[nx][ny] and board[nx][ny] < sharkSize:
                        minDist = d
                        dist.append((d + 1, nx, ny))
                    if d + 1 <= minDist:
                        q.append((nx, ny, d + 1))
    if dist:
        dist.sort()
        return dist[0]

    else:
        return

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = []
    sharkSize = 2
    eat = 0
    eatCnt = 0
    sharkX, sharkY = 0, 0
    fishCnt = 0
    fishPosition = []
    time = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(n):
        line = list(map(int, input().split()))
        board.append(line)
        for j in range(n):
            if line[j] == 9:
                sharkX, sharkY = i, j
            elif 0 < line[j] and line[j] < 7:
                fishCnt += 1
                fishPosition.append([i,j])
    board[sharkX][sharkY] = 0

    while fishCnt:
        res = bfs(sharkX, sharkY)
        if not res:
            break
        sharkX, sharkY = res[0], res[1]
        time += res[2]
        eat += 1
        if sharkSize == eat:
            sharkSize += 1
            eat = 0
        board[sharkX][sharkY] = 0

    print(time)