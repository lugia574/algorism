# 이게 문제가 뭐냐면
# 국경선 경우하는 경우가 꼭 한 그룹으로 될 리가 없자나
# A 그룹 있고 B 그룹 있을 수 있는건데 다 하나로 퉁쳐버려
# 그래서 그거를 보완해서 하니까 먼가 전체의 값이 증가되는듯??? 뭐가 문제냐 ㅋㅋ

# https://pacific-ocean.tistory.com/375
# 나랑 비슷한거 같은데?? 내가 뭐 실수 한듯?
from collections import deque
import sys

input = sys.stdin.readline
def bfs(i, j):
    q = deque()
    q.append([i, j])
    temp = []
    temp.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(s[nx][ny] - s[x][y]) <= r:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    temp.append([nx, ny])
    return temp
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
cnt = 0
while True:
    visit = [[0] * n for i in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i, j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum([s[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        s[x][y] = num
    if not isTrue:
        break
    cnt += 1
print(cnt)

# import sys
# from collections import deque
#
# def BFS():
#     s = set()
#     while q:
#         x, y= q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
#                 gap = abs(country[x][y] - country[nx][ny])
#                 if l <= gap <= r:
#                     s.add((x, y))
#                     s.add((nx, ny))
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
#     if len(s) > 0:
#         setArray.append(s)
#
# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n, l, r = map(int, input().split())
#     country = [list(map(int, input().split())) for _ in range(n)]
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     day = -1
#     q = deque()
#     while True:
#         setArray = []
#         day += 1
#         visited = [[0] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 if visited[i][j] == 0:
#                     q.append((i, j))
#                     visited[i][j] = 1
#                     BFS()
#
#         length = len(setArray)
#         if length == 0: break
#
#         sumPeople = 0
#         for s in range(length):
#             setLength = len(setArray[s])
#             for x, y in setArray[s]:
#                 sumPeople += country[x][y]
#             meanPeople = sumPeople // setLength
#
#             for x, y in setArray[s]:
#                 country[x][y] = meanPeople
#         print("==========")
#         for x in country:
#             print(x)
#     print(day)
