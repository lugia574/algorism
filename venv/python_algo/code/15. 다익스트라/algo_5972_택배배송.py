
    import sys, heapq

    def dijkstra():
        hq = []
        heapq.heappush(hq, (0, 1))
        dp[1] = 0

        while hq:
            weight, now = heapq.heappop(hq)
            if dp[now] < weight: continue

            for nextWeight, nextNode in graph[now]:
                nextWeight += weight
                if dp[nextNode] > nextWeight:
                    dp[nextNode] = nextWeight
                    heapq.heappush(hq, (nextWeight, nextNode))

    if __name__ == "__main__":
        input = sys.stdin.readline
        INF = sys.maxsize
        n, m = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append((c, b))
            graph[b].append((c, a))

        dp = [INF] * (n+1)
        dijkstra()
        print(dp[n])

