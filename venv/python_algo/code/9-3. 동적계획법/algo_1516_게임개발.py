import sys
from collections import deque

def simCity(n):
    seq = [[] for _ in range(n+1)] # 건설 순서 규칙
    inDegree = [0] * n # 진입찻수
    dp = [0] * n
    q = deque()
    cost = []
    # 건설 순서 및 진입차수 없는 애는 바로 dp로 박을 꺼임
    for i in range(n):
        build = list(map(int, input().rsplit()))
        cost.append(build[0])
        if build[1] == -1:
            dp[i] = build[0]
            q.append(i)

        for x in build[1:]:
            if x == -1:
                break
            seq[x-1].append(i)
            inDegree[i] += 1

    while q:
        b = q.popleft()
        for x in seq[b]:
            inDegree[x] -= 1
            dp[x] = max(dp[b] + cost[x], dp[x])
            if inDegree[x] == 0:
                q.append(x)

    return dp

if __name__== "__main__":
    input = sys.stdin.readline
    n = int(input())
    res = simCity(n)
    for i in res:
        print(i)
