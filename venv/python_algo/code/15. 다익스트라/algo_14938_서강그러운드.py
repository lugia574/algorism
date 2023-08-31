# 아직도 졸려요~ 보니깡 각각 n 번씩 조져서 값 비교해서 갱신하는 형태로 가야하지 않을까나??
# 범위도 n 100임 시복따윈 안결려~
# 각 최소점수 구해서 그 점수가 r 보다 작으면 쌉가능인 부분들을 합합합 해서 값비교~
# 아니 시벌 내가 뭔실수를 했길래 안됨?
# https://donghak-dev.tistory.com/86 존나 빡치네
# 뭐냐 시발 진짜 개빡치네 안해 시발

import sys, heapq

def dijkstra(start):
    dist = [INF] * (n + 1)
    hq = []

    heapq.heappush(hq, [0, start])
    dist[start] = 0

    while hq:
        w, now = heapq.heappop(hq)

        for nextWeight, nextNode in graph[now]:
            if dist[nextNode] > nextWeight + w:
                nextWeight += w
                dist[nextNode] = nextWeight
                heapq.heappush(hq, [nextWeight, nextNode])

    return dist


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    n, m, r = map(int, input().split())
    costArr = list(map(int, input().split()))
    costArr.insert(0, 0)

    graph = [[] for _ in range(n+1)]
    res = int(-1e9)

    for _ in range(r):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    for i in range(1, n+1):
        groupSumVal = 0
        distance = dijkstra(i)
        for i in range(1, n+1):
            if distance[i] <= r:
                groupSumVal += costArr[i]

        res = max(res, groupSumVal)

    print(res)