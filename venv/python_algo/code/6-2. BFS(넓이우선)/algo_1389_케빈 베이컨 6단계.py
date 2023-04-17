import sys
from collections import deque

def SixDegrees(n, m):
    seq = [[] for _ in range(n+1)] # 연결 순서
    q = deque()
    cost = [0] * (n+1)

    # 연결순서 주입
    for _ in range(m):
        s, e = map(int, input().rsplit())
        seq[s].append(e)
        seq[e].append(s)

    for i in range(1, n+1):
        check = [0] * (n+1)
        q.append((i,1))
        check[i] = 1
        while q:
            x, c = q.popleft()
            for j in seq[x]:
                if check[j] == 0:
                    check[j] = 1
                    cost[i] += c
                    q.append((j, c+1))

    return cost.index(min(cost[1:]))

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().rsplit())
    res = SixDegrees(n, m)
    print(res)