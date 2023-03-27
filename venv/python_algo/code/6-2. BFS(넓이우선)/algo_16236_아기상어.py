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


# 자

import sys
from collections import deque

def bfs(sharkX, sharkY):
    q = deque()
    q.append((sharkX, sharkY))

    visted = [[0] * n for _ in range(n)]
    visted[sharkX][sharkY] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if sharkSize >= board[nx][ny] and visted[nx][ny] == 0:
                    visted[nx][ny] = visted[x][y] + 1
                    q.append((nx, ny))
    return visted

def eating(visited):
    x, y = 0, 0
    min_dis = INF
    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0 and 0 < board[i][j] < sharkSize:
                if visited[i][j] < min_dis:
                    min_dis = visited[i][j]
                    x, y = i, j

    if min_dis == INF:
        return False
    else:
        return x, y, min_dis

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    sharkSize = 2
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    INF = 1e9
    nowX, nowY = 0, 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                nowX, nowY = i, j
                board[i][j] = 0

    res = 0
    food = 0

    while True:
        visted = bfs(nowX,nowY)
        position = eating(visted)

        if not position:
            print(res)
            break
        else:
            nowX, nowY, dis = position
            res += dis
            board[nowX][nowY] = 0
            food += 1

        if food >= sharkSize:
            sharkSize += 1
            food = 0


