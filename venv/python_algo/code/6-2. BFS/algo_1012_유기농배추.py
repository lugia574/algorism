# 1. 아이디어
# 단지 번호 붙이기랑 같음
# num 붙혀서 cnt 세면 됨
# 값 받는것만 잘 받아서 배열에 박아주면 됨
import sys
from collections import deque
def BFS(y, x, num):
    global farm

    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()

        for i in range(4):
            yy = dy[i] + y
            xx = dx[i] + x
            if 0 <= yy < n and 0 <= xx < m and farm[yy][xx] == 1:
                q.append((yy, xx))
                farm[yy][xx] = num



if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        num = 2
        m, n, k = (list(map(int, input().split())))
        farm = [[0] * m for _ in range(n)]

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for _ in range(k):
            x, y = map(int, input().split())
            farm[y][x] = 1
        for i in range(n):
            for j in range(m):
                if farm[i][j] == 1:
                    farm[i][j] = num
                    BFS(i,j, num)
                    num += 1
        print(num-2)