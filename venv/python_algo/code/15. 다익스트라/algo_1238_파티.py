# 이번에는 각 애새끼들 돌면서 가장 먼새끼를 부르라는데
# 그럼 무조건 N 번씩 돌려야한다는 소리 아니니니니님ㅁ???
# 기존의 다익스트라 하면 좀 빡세지 않을까나나나나나나나????
# 우선 걍 박아봐 ㅋ 다익스트라가 대충 Elog(N) 이니까 어떻게든 되것지 ㅋㅋ
# 아아아아 오고 가야해 오고 가야한다고 쓰으읍 이거 시초 안되려나 모르겠네
# 크으으으윽 이게 섹스지~
import sys, heapq, copy

def dijkstra(start):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        w, now = heapq.heappop(heap)
        if dp[now] < w: continue

        for nextNode, nextW in graph[now]:
            nextW += w
            if nextW < dp[nextNode]:
                dp[nextNode] = nextW
                heapq.heappush(heap, (nextW, nextNode))


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    INF = 100 * n + 1
    dp = [INF] * (n + 1)
    res = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(x)
    distX = copy.copy(dp)
    
    for s in range(1, n+1):
        if s == x: continue
        dp = [INF] * (n+1)
        dijkstra(s)
        length = dp[x] + distX[s]
        heapq.heappush(res, length * -1)

    print(heapq.heappop(res) * -1)
