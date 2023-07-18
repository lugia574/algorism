# 기존 방식에서 조금더 효율적으로 처리 하는 방법은
# dp 를 이용해 2^i 급으로 거슬러 올라가는거임
# 세그먼트 트리를 이용해도 됨
# 매 쿼리마다 거슬러 M logN 의 복잡도를 가짐

import sys
sys.setrecursionlimit(int(1e9))

def depthCheck(x, d):
    check[x] = True
    depth[x] = d

    for y in graph[x]:
        if check[y]: continue
        parent[y][0] = x
        depthCheck(y, d+1)

def setParent():
    depthCheck(1, 0)

    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(LOG -1, -1 , -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a
    for i in range(LOG - 1 , -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]
if __name__ == "__main__":
    input = sys.stdin.readline
    LOG = 21
    n = int(input())

    parent = [[0] * LOG for _ in range(n+1)]
    depth = [0] * (n+1)
    check = [0] * (n+1)

    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    setParent()

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        print(lca(a, b))



