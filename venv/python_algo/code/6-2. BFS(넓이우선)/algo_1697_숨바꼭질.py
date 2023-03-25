# 1. 아이디어
# 아니 이걸 어떻게 BFS 로 품?


import sys
from collections import deque

def BFS(n):
    global check
    global limit
    q = deque()
    q.append(n)
    LEVEL = 1

    while q:
        x = q.popleft()
        arr = [x - 1, x + 1, x * 2]
        if x == k:
            break
        for val in arr:
            if 0 <= val < limit and check[val] == 0:
                q.append(val)
                check[val] = check[x] + LEVEL



if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    limit = 10 ** 5 * 2
    check = [0] * (limit + 1)

    BFS(n)
    print(check[k])

