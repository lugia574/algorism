# 1. 아이디어
# 이건 BFS, DFS 둘다 풀 수 있음
# 우선은 BFS 로 풀어볼꺼임
# check 리스트를 만들고
# q에 0,0 을 박고 dx, dy 를 돌면서 1 인 값을 찾아 가는거지
# 그래서 q에 계속 박아
# 그렇게 도착을 하면 cnt 값을 return 하면 될꺼 같애
# 2. 시간 복잡도
# 음 4번 돌테고 총 n 하겠고 흠 4n 할껄?

from collections import deque

def BFS (n,m,maze):
    q = deque()
    q.append((0,0))
    while q:
        y, x = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < m and 0 <= yy < n and maze[yy][xx] == 1:
                q.append((yy, xx))
                maze[yy][xx] = maze[y][x] + 1

    return maze[n-1][m-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    print(maze)
    res = BFS(n, m, maze)
    print(res)