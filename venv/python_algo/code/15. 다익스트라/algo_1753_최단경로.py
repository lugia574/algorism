# 내가 푼 방식은 플루로이드 워샬 알고리즘 방식으로
# 이렇게 하니까 메모리 초과가 되버리네~
# 다익스트라 알고리즘은 하나의 정점에서 나머지 모든 정점까지의 최단 거리를 찾는 알고리즘이다.
# 모든 정점의 최단거리를 구하는 플로이드-워셜 알고리즘과 다른 알고리즘이니 착각하지 말자!
# 라네~

# https://www.youtube.com/watch?v=611B-9zk2o4&t=472s
import sys
import heapq


def dijkstra(start):
    heap = []
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, now = heapq.heappop(heap)
        if dp[now] < weight:
            continue
        for nexWeight, nextNode in graph[now]:
            nexWeight += weight

            if nexWeight < dp[nextNode]:
                dp[nextNode] = nexWeight
                heapq.heappush(heap, (nexWeight, nextNode))

if __name__ == "__main__":
    input = sys.stdin.readline
    INF = 11
    V, E = map(int, input().split())
    #시작점 K
    K = int(input())
    #가중치 테이블 dp
    dp = [INF]*(V+1)
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))

    dijkstra(K)
    for i in range(1, V+1):
        print("INF" if dp[i] == INF else dp[i])



# if __name__ == "__main__":
#     input = sys.stdin.readline
#     v, e = map(int, input().split())
#     s = int(input())
#     nodes = [[11] * (v+1) for _ in range(v+1)]
#     for _ in range(e):
#         x, y, z = map(int, input().split())
#         nodes[x][y] = z
#
#     for k in range(1, v+1):
#         for i in range(1, v+1):
#             for j in range(1, v+1):
#                 nodes[i][j] = min(nodes[i][j], nodes[i][k] + nodes[k][j])
#
#     for i in range(1, v+1):
#         if i == s:
#             print(0, end=" ")
#         else:
#             print(nodes[s][i] if nodes[s][i] < 10 else "INF", end=" ")