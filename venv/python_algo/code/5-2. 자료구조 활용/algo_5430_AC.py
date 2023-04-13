import sys
from collections import deque

def cmd(p, arr, n):
    rev = False
    if n == 0:
        arr = []

    for c in p:
        if c == "R":
            rev = False if rev else True
        else:
            if len(arr) == 0:
                return False
            if rev:
                arr.pop()
            else:
                arr.popleft()

    if rev:
        arr.reverse()
    return True


if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        p = list(input())
        n = int(input())
        arr = deque(input()[1:-1].split(","))

        res = cmd(p, arr, n)
        print("["+",".join(arr)+"]" if res else "error")

