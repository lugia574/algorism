# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은
# 토마토의 영향을 받아 익게 된다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들
# 의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로
# 그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
# ▣ 입력설명
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다. M은 상자의 가로 칸의 수, N
# 은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M, N ≤ 1,000 이다.
# 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄
# 에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토
# 의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수
# -1은 토마토가 들어있지 않은 칸을 나타낸다.
# ▣ 출력설명
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든
# 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을
# 출력해야 한다.
# ▣ 입력예제 1
# 6 4
# 0 0 -1 0 0 0
# 0 0 1 0 -1 0
# 0 0 -1 0 0 0
# 0 0 0 0 -1 1
# ▣ 출력예제 1
# 4
from collections import deque

def tomatoBFS():
    global day

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < m and 0 <= yy < n:
                    if tomato[xx][yy] == 0:
                        tomato[xx][yy] = tomato[x][y] + 1
                        q.append((xx, yy))
                        day = tomato[xx][yy] - 1



if __name__ == "__main__":
    n, m = map(int, input().split())
    day= 0
    q = deque()
    tomato = [list(map(int,input().split())) for _ in range(m)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(m):
        for j in range(n):
            if tomato[i][j] == 1:
                q.append((i,j))
    tomatoBFS()

    result = True
    for i in range(m):
        for j in range(n):
            if tomato[i][j] == 0:
                result = False
                break

    print(day if result else -1)