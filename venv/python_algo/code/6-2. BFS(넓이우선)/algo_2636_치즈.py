# 대체 치즈 안의 구멍을 어떻게 구분하냐 존나 모르겠었는데
# 다 방법이 있더라 시벌
# 그건 바로 반대로 치즈를 타고 도는게 아니라 바깥 0 부분을 타고 도는거임
# 그럼 치즈 안에 빈 공간은 절대로 탈 수 가 없음
# 바깥을 돌면서 접촉되는 치즈 부위만 따로 배열에 박아서 포문 돌면서 0 으로 만들어 주면 됨
import math
import sys
from collections import deque

def BFS(a, b):
    q.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0:
                if board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    visited[nx][ny] = 2
                    outlineCheese.append((nx, ny))

    for cx, cy in outlineCheese:
        board[cx][cy] = 0

    return len(outlineCheese)

if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(r)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    day = -1
    cheese = math.inf
    while True:
        day += 1
        q = deque()
        outlineCheese = []
        visited = [[0] * c for _ in range(r)]
        tmp = BFS(0,0)

        if tmp == 0:
            break
        else:
            cheese = tmp

    print(day)
    print(cheese)