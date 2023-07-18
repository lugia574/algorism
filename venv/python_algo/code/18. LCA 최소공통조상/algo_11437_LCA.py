# https://bbbyung2.tistory.com/76
# 이건 입력값이 그렇게 많지 않을때 가능
# 근데 뭐 테스트케이스가 추가됐는지 안되네 ㅋㅋ

import sys
sys.setrecursionlimit(10**6)

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

def depthCheck(x, d):
    check[x] = True
    depth[x] = d
    for y in graph[x]:
        if check[y]: continue
        parent[y] = x
        depthCheck(y, d+1)

if __name__ == "__main__":
    n = int(input())

    parent = [0] * (n+1)
    depth = [0] * (n+1) # 깊이
    check = [False] * (n+1)

    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    depthCheck(1, 0)

    m = int(input())

    for i in range(m):
        a, b = map(int, input().split())
        print(lca(a, b))
