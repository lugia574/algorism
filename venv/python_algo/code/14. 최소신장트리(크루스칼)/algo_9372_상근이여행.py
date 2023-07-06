# 아 졸려요 졸려

import sys

def getParent(a):
    if parent[a] != a:
        parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b):
    global cnt
    a = getParent(a)
    b = getParent(b)
    if a == b:
        return

    cnt += 1
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n, m = map(int, input().split())
        parent = [i for i in range(n+1)]
        cnt = 0
        for _ in range(m):
            a, b = map(int, input().split())
            if getParent(a) != getParent(b):
                unionParent(a, b)
        print(cnt)