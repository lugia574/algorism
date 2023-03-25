import sys

def bfs():
    global cnt
    queue = set([(0, 0, graph[0][0])]) # 시간 초과를 줄이기 위해 중복되는 곳은 제거

    while queue:
        x, y, z = queue.pop()

        # 말이 지날 수 있는 최대의 칸 초기화
        cnt = max(cnt, len(z))

        # 상/하/좌/우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고 알파벳이 중복이 안된다면 탐색
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in z:
                queue.add((nx, ny, graph[nx][ny] + z))


r, c = map(int, sys.stdin.readline().split())

graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1

bfs()
print(cnt)

# input = sys.stdin.readline
# r, c = map(int, input().split())
# arr = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]
# alpha = [0] * 26
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# def dfs(x, y, count):
#     global ans
#     ans = max(ans, count)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c and alpha[arr[nx][ny]] == 0:
#             alpha[arr[nx][ny]] = 1
#             dfs(nx, ny, count + 1)
#             alpha[arr[nx][ny]] = 0
#
#
# ans = 1
# alpha[arr[0][0]] = 1
# dfs(0, 0, 1)
#
# print(ans)