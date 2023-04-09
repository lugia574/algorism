from collections import deque
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    q = deque()
    for _ in range(t):
        cmd = input().split()
        if cmd[0] == "push":
            q.append(int(cmd[1]))
        elif cmd[0] == "pop":
            if len(q) > 0:
                num = q.popleft()
                print(num)
            else:
                print(-1)
        elif cmd[0] == "size":
            print(len(q))
        elif cmd[0] == "empty":
            print(0 if len(q) > 0 else 1)
        elif cmd[0] == "front":
            print(q[0] if len(q) > 0 else -1)
        elif cmd[0] == "back":
            print(q[-1] if len(q) > 0 else -1)
