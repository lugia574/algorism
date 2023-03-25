# ?? 이거 dp 문제 맞음?
# 이거 그냥 DFS, BFS 문제 아님?
# m, n 도 500 이니까 2초면 충분히 쌉가능일꺼 같은데

# 시초 떳다 ㅅㅂ
# https://limepencil.tistory.com/5 이걸 보자


import sys
import heapq

def BFS():
    queue = [(-table[0][0],0,0)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        h, x, y = heapq.heappop(queue)
        for dx, dy in direction:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m and table[nx][ny] < table[x][y]:
                if visited[nx][ny] ==0:
                    heapq.heappush(queue,(-table[nx][ny],nx,ny))
                visited[nx][ny] += visited[x][y]
    return visited[n-1][m-1]

input = sys.stdin.readline
n,m = map(int,input().split())
table = [list(map(int,input().split()))for _ in range(n)]
print(BFS())


# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque
#
# if __name__ == "__main__":
#     input = sys.stdin.readline
#     m, n = map(int, input().split())
#     map = [list(map(int, input().split())) for _ in range(m)]
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     q = deque()
#     check = [[0] * n for _ in range(m)]
#     q.append((0,0))
#
#     while q:
#         x, y = q.popleft()
#         check[x][y] += 1
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if map[x][y] > map[nx][ny]:
#                     q.append((nx, ny))
#
#
#     print(check[m-1][n-1])

    # for i in check:
    #     print(i)