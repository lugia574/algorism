import sys
from collections import deque

def bfs(a,b):
    q = deque()
    q.append((a, 0))
    check[a] = 1
    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt
        for i in seed[x]:
            if check[i] == 0:
                q.append((i, cnt + 1))
                check[i] = 1
    return -1


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    check = [0] * (n + 1)
    a, b = map(int, input().split())
    m = int(input())
    seed = [[] for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        seed[i].append(j)
        seed[j].append(i)

    res = bfs(a, b)

    print(res)