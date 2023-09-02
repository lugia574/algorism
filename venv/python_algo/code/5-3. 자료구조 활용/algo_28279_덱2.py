import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    q = deque()
    for _ in range(n):
        order = list(map(int, input().split()))
        if order[0] == 1:
            q.appendleft(order[1])
        elif order[0] == 2:
            q.append(order[1])
        elif order[0] == 3:
            print(q.popleft() if len(q) > 0 else -1)
        elif order[0] == 4:
            print(q.pop() if len(q) > 0 else -1)
        elif order[0] == 5:
            print(len(q))
        elif order[0] == 6:
            print(1 if len(q) == 0 else 0)
        elif order[0] == 7:
            print(q[0] if len(q) > 0 else -1)
        elif order[0] == 8:
            print(q[-1] if len(q) > 0 else -1)