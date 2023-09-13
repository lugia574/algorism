# DFS 로 조져야하나 생각했는데
# 보니까 유니파인드 문제네
# 근데 카테고리 보면 깊이 우선 탐색도 있던데 가능은 할듯?
# https://imksh.com/60

import sys

def getParent(x):
    if x == parent[x]: return x
    parent[x] = getParent(parent[x])
    return parent[x]


def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a == b: return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    input = sys.stdin.readline
    direction = dict()
    direction['D'] = [0, 1]
    direction['L'] = [-1, 0]
    direction['R'] = [1, 0]
    direction['U'] = [0, -1]

    N, M = map(int, input().split())
    field = [list(input().strip()) for _ in range(N)]
    parent = [i for i in range(N * M)]

    for num in range(N * M):
        x = num // M
        y = num % M
        cur = field[x][y]
        nx = x + direction[cur][1]
        ny = y + direction[cur][0]
        next_num = nx * M + ny
        if next_num < 0 or next_num >= N * M: continue
        unionParent(num, next_num)

    answer = 0
    visited = dict()
    for i in range(N * M):
        if getParent(parent[i]) not in visited:
            answer += 1
            visited[parent[i]] = True
    print(answer)