# 다익스트라에 조건하나 더 붙은거네
# 꼭 거쳐야하는 노드가 있는데
# 어차피 시작점은 1 번이고 그리고 노드 2개를 거치고 나서 n 노드로 골인하는거자너?
# 그럼 그냥 1 > 노드1 > 노드2 > n 으로 해버리면 되지 않을까? 노드2 > 노드 1 의 가능성도 있으니까 두개 구해서 비교때려서 해버리면 되자너

# 그럴려면 각 정점을 시작으로 했을떄의 최단경로 배열을 각각 구해 1 과 노드1, 노드2 이렇게
# 그래서 시작점 1 > 노드 1 로 갈때 최단경로 + 노드 1 > 노드 2 최단 경로 + 노드 2 > 마지막 N 으로 갈때 이렇게 값을 구하는거야

import sys
import heapq

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for nextNode, nextCost in graph[now]:
            nextCost += dist
            if distance[nextNode] > nextCost:
                distance[nextNode] = nextCost
                heapq.heappush(q,(nextNode, nextCost))

    return distance

if __name__ == "__main__":
    input = sys.stdin.readline
    n, e = map(int, input().split()) # 노드, 간선 갯수
    INF = sys.maxsize
    graph = [[] for _ in range(n+1)]

    for _ in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append([b, cost])
        graph[b].append([a, cost])
    node1, node2 = map(int, input().split())


    originDistance = dijkstra(1)
    n1Distance = dijkstra(node1)
    n2Distance = dijkstra(node2)

    route1 = originDistance[node1] + n1Distance[node2] + n2Distance[n]
    route2 = originDistance[node2] + n2Distance[node1] + n1Distance[n]

    result = min(route1, route2)
    print(result if result < INF else -1)