# 이런 정렬을 안해줘서 틀린거였는데 그걸 몰라서 헤맸네
import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k, x = map(int, input().split())
    nodes = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        nodes[a].append(b)

    visited = [0] * (n + 1)
    q = deque()
    res = []
    q.append((x, 0))
    visited[x] = 1

    while q:
        now, dist = q.popleft()
        if dist == k:
            res.append(now)
        if dist > k:
            continue
        for next_node in nodes[now]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append((next_node, dist + 1))

    if res:
        res.sort()
        for r in res:
            print(r)
    else:
        print(-1)
