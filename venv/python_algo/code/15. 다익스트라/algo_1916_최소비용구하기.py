# 띠요용 시초가 뜨녜녜녜??
# if dp[now] < cost: continue 이걸 해주니까 됨
# 대에충 결국 최적을 구하기 위해 그리디 하게 싹 훑고 지나가니까 이미 cost 보다 작게 나오면
# 어차피 다음 노드에서 나온 cost 더한들 의미 없으니까 커트 쳐버린다 이런거지
import sys, heapq

def dijkstra(start):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cost, now = heapq.heappop(heap)
        # 이걸 해주니꺼 걸러주네
        if dp[now] < cost: continue
        for nextNode, nextCost in graph[now]:
            nextCost += cost

            if nextCost < dp[nextNode]:
                dp[nextNode] = nextCost
                heapq.heappush(heap, (nextCost, nextNode))

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    INF = 100_000 * n + 1
    graph = [[] for _ in range(n+1)]
    dp = [INF] * (n+1)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))


    start, end = map(int, input().split())
    dijkstra(start)

    print(dp[end])