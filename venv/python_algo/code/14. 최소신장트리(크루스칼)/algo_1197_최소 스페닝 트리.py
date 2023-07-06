import sys

def getParent(a):
    if parent[a] != a:
        parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b, c):
    global res
    a = getParent(a)
    b = getParent(b)
    if a == b:
        return
    res += c
    if a < b : parent[b] = a
    else: parent[a] = b

if __name__ == "__main__":
    input = sys.stdin.readline
    v, e = map(int, input().split())
    parent = [i for i in range(v+1)]
    edge = [list(map(int, input().split())) for _ in range(e)]
    edge.sort(key=lambda x: x[2])
    res = 0
    for x, y, c in edge:
        if getParent(x) != getParent(y):
            unionParent(x, y, c)

    print(res)

