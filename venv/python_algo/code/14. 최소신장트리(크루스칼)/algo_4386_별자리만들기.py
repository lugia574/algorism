import math
import sys

def getParent(a):
    if parent[a] != a:
        parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b, c):
    global res
    a = getParent(a)
    b = getParent(b)
    if a == b: return
    if a < b: parent[a] = b
    else: parent[b] = a
    res += c

# a^2 + b^2 = c^2
def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    parent = [i for i in range(n)]
    planet = [list(map(float, input().split())) for _ in range(n)]
    distance = []
    for i in range(n-1):
        for j in range(i + 1, n):
            d = dist(planet[i], planet[j])
            distance.append((i, j, d))
    distance.sort(key=lambda x:x[2])

    res = 0
    # print(distance)
    for a, b, c in distance:
        if getParent(a) != getParent(b):
            unionParent(a, b, c)

    print(math.floor(res, 2))

