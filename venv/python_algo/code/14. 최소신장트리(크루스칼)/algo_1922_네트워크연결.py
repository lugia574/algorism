# 이 문제는 크루스칼 알고리즘을 사용해야함
# 유니온파인드를 이용함

import sys

# 부모노드 찾기
def getParent(parent, x):
    if parent[x] == x:
        return x

    parent[x] = getParent(parent, parent[x])
    return parent[x]

# 부모노드 합치기
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 같은 부모를 가지고 있는지 확인
def findParent(Parent, a, b):
    a = getParent(Parent, a)
    b = getParent(Parent, b)
    if a == b: return 1
    return 0

if __name__== "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    nodes = [[0] * (n) for _ in range(n)]
    parent = [i for i in range(n+1)]
    route = [list(map(int, input().split()) )for _ in range(m)]
    route.sort(key=lambda x: x[2])
    tc = 0
    for r in route:
        x, y, c = r
        if findParent(parent, x, y) == 0:
            unionParent(parent, x, y)
            tc += c
        if(sum(parent) == n):
            break

    print(tc)
