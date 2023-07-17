import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    q = deque()
    res = []
    for i in range(1, n+1):
        q.append(i)

    for _ in range(n-1):
        res.append(q.popleft())
        q.append(q.popleft())

    print(*res, *q)