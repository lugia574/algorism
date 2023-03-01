# 1. 아이디어
# 단지 이름 붙이기니까 for 문 돌면서 1 나오는 순간 바로 BFS 에 박아버려
# BFS 는 해당 단지들 싹다 번호 지정해버리고 갯수를 apartComplex 에 박아
# len apar 이랑 각각 값들 풀어내면 끝

import sys
from collections import deque

def BFS(loc , nom):
    global apart
    global group
    q = deque()
    q.append(loc)
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and apart[yy][xx] == 1:
                q.append((yy, xx))
                apart[yy][xx] = nom
    group.append(cnt)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    apart = [list(map(int, input().rstrip())) for _ in range(n)]
    num = 2
    group = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            if apart[i][j] == 1:
                apart[i][j] = num
                BFS((i, j), num)
                num += 1

    group.sort()
    print(len(group))
    for i in group:
        print(i)
