# N (2 ≤ N ≤ 100,000)
import sys
from collections import deque


def BFS(v):
    q = deque()
    q.append(v)

    while q:
        node = q.popleft()
        for i in tree[node]:
            if visited[i] == 0:
                visited[i] = node
                q.append(i)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    tree = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(n-1):
        x, y= map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)

    BFS(1)

    for i in tree:
        print(i)

    for i in range(2,n+1):
        print(visited[i])