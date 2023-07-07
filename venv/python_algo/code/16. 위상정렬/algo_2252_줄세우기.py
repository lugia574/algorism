import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    answer = []
    inDegree = [0] * (n+1)
    q = deque()

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        height = q.popleft()
        answer.append(height)
        for i in graph[height]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                q.append(i)

    print(*answer)