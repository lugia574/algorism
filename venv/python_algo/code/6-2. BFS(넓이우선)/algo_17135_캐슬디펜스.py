import sys
from collections import deque

def posComb(l, k):
    if l == 3:
        attack(castle)
        return
    for i in range(k, m):
        castle.append(i)
        posComb(l+1, i+1)
        castle.pop()

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, d = map(int, input().rsplit())
    board = [list(int, input().rsplit()) for _ in range(n)]

    kill = 0
    castle = []
    posComb(0, 0)
