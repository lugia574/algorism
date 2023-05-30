import sys
from collections import deque

def BFS(b):
    q = deque()
    q.append(b)
    check = [0] * (n+1)
    check[b] = 1
    while q:
        x = q.popleft()
        for y in node[x]:
            if check[y] == 0:
                q.append(y)
                check[y] = 1
    return sum(check)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().rsplit())
    node = [[] for _ in range (n+1)]
    dp = [0] * (n+1)
    res = []
    maxCnt = 0

    for _ in range(m):
        a, b = map(int, input().rsplit())
        node[b].append(a)

    for i in range(1, n+1):
        if node[i]:
            cnt = BFS(i)
            if cnt > maxCnt:
                maxCnt = cnt
                res = [i]
            elif cnt == maxCnt:
                res.append(i)
    print(*res)