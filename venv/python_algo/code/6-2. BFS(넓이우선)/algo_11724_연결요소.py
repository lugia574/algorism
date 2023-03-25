import sys
from collections import deque

def BFS(e):
    global check

    q = deque()
    q.append(e)
    while q:
        x = q.popleft()
        check[x] = True
        for k in node[x]:
            if not check[k]:
                q.append(k)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    node = [[] for _ in range(n+1)]
    check = [False] * (n+1)
    cnt = 0

    for _ in range(m):
        x, y = map(int, input().split())
        node[x].append(y)
        node[y].append(x)

    for i in range(1, n+1):
        if not check[i]:
            if node[i]:
                BFS(i)
            else:
                check[i] = True
            cnt += 1

    print(cnt)


# 시벌 py 으로 하니까 ㅈㄹ 남