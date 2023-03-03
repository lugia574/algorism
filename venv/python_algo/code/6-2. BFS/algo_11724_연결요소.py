import sys
from collections import deque
# sys.setrecursionlimit(10**7)

def BFS(e):
    global check

    q = deque()
    q.append(e)
    while q:
        x = q.popleft()
        check[x] = 1
        for k in node[x]:
            if check[k] == 0:
                q.append(k)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    node = [[] for _ in range(n+1)]
    check = [0] * (n+1)
    cnt = 0
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        node[x].append(y)
        node[y].append(x)

    for i in range(1, n+1):
        if check[i] == 0:
            if node[i]:
                BFS(i)
            else:
                check[i] = 1
            cnt += 1

    print(cnt)


# 시벌 py 으로 하니까 ㅈㄹ 남