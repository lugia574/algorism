# 먼데
import sys
from collections import deque

def BFS():
    q = deque()
    q.append(n)

    while q:
        s = q.popleft()
        if s == k:
            break
        if 0 <= s - 1 < 100001 and visited[s - 1] == -1:
            visited[s - 1] = visited[s] + 1
            q.append(s - 1)
        if 0 < s * 2 < 100001 and visited[s * 2] == -1:
            visited[s * 2] = visited[s]
            q.appendleft(s * 2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
        if 0 <= s + 1 < 100001 and visited[s + 1] == -1:
            visited[s + 1] = visited[s] + 1
            q.append(s + 1)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    move = [2, 1, -1]
    visited = [-1 for _ in range(100001)]
    visited[n] = 0
    BFS()
    print(visited[k])