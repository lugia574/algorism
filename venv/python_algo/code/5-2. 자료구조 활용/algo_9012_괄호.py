import sys
from collections import deque
if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        q = deque()
        bracket = list(map(str, input()))
        res = 1
        for x in bracket:
            if x == "(":
                q.append(x)
            else:
                if q:
                    q.popleft()
                else:
                    res = 0
                    break
        if q:
            res = 0

        print("YES" if res == 1 else "NO")
