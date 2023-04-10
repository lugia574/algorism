import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    q = deque()
    for i in range(1, n+1):
        q.append(i)

    while len(q) > 1:
        q.popleft()
        firstNum = q.popleft()
        q.append(firstNum)

    print(q[0])