import math
from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    q = deque()
    q.append((graph[1], 0))
    visited = [0] * (n+1)
    visited[1] = -1
    while q:
        li, x = q.popleft()
        for i in li:
            if visited[i] == 0:
                visited[i] = x + 1
                q.append((graph[i], x + 1))
    maxVal = max(visited)
    for i in range(1, n+1):
        if visited[i] == maxVal: answer += 1
    return answer

if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    res = 3
    ans = solution(n, edge)
    print(res == ans)