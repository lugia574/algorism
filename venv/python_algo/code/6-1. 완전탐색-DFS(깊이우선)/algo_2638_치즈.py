# 또 까먹었는데
# 겉만 슥 핥으려면 1를 팔게 아니라 0 부터 슥 가야하는거여
import sys
from collections import deque
def check(x, y):
    air = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 1:
                air += 1
                if air > 1:
                    return True
    return False

def BFS():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 2
                    removeArr.append((nx, ny))

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().rsplit())
    board = [list(map(int, input().rsplit())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    time = 0
    while True:
        removeArr = []
        visited = [[0] * m for _ in range(n)]
        BFS()
        # print("========")
        # for x in visited:
        #     print(x)
        if not removeArr:
            break
        # print(removeArr)
        for x, y in removeArr:
            if check(x, y):
                board[x][y] = 0
        time += 1

    print(time)



# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 1 1 1 0 1 1 0 0
# 0 1 0 1 1 1 1 0 0
# 0 0 1 1 0 0 0 1 0
# 0 0 1 1 1 1 1 1 0
# 0 1 1 0 0 1 1 1 0
# 0 0 1 0 0 1 0 1 0
# 0 0 0 0 0 0 0 0 0

# 3


# 11 15
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 0 1 0 0 0 1 0 0
# 0 0 1 0 1 1 1 1 0 1 1 1 0 1 0
# 0 0 1 1 0 1 0 0 1 1 1 0 1 1 0
# 0 0 1 0 1 0 1 1 1 1 1 1 0 1 0
# 0 0 1 0 0 0 1 1 0 0 1 0 1 0 0
# 0 1 1 0 1 0 0 0 0 1 1 1 0 0 0
# 0 1 1 0 1 1 1 0 1 1 1 1 1 1 0
# 0 0 0 1 1 0 1 0 1 0 0 0 0 1 0
# 0 0 0 0 0 1 0 1 0 1 0 0 0 1 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 4

# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0

# 3