
import sys

def getParent(a):
    if a == parent[a]:
        return a
    parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b):
    a = parent[a]
    b = parent[b]
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    input = sys.stdin.readline
    while True:
        m, n = map(int, input().split())
        if m + n == 0:
            break
        routes = [list(map(int, input().split())) for _ in range(n)]
        routes.sort(key=lambda x: x[2])
        parent = [i for i in range(m)]
        totalCost = 0
        savedCost = 0
        for a, b, c in routes:
            if getParent(a) != getParent(b):
                unionParent(a, b)
                savedCost += c
            totalCost += c

        print(totalCost - savedCost)