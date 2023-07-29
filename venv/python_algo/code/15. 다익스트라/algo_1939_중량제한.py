# 시이발 메모리초과 먼데~
# https://velog.io/@ckstn0778/백준-1939번-중량제한-1-Python
# 보니까 다익스트라로 푸는데
# 솔직히 까먹었음 ㅋㅋ 하 몇주전에 풀었던건데 ㅋ
# 워샬로 푸니까 어김없이 터져버리고 ㅋ

import heapq, sys

input = sys.stdin.readline

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)  # 최대힙
        # 이전 중량
        dist = -1 * dist

        if now == end:
            print(dist)
            break

        if distance[now] > dist: # 이미 최대 중량인경우
            continue

        for i in graph[now]: # 정렬된 상태이므로 높은 중량부터 탐색이 됨.
            d, node = i
            if dist == 0: # dist가 0인게 문제여...
                distance[node] = d
                heapq.heappush(queue, (-distance[node], node))
            # 기존에 저장된 값이 dist(이전 도시에서의 최대중량)와 현재 다리 최대 중량 보다 작다면...
            # 이렇게 한 이유는 다리가 중복 연결되어있는 가능성이 있기 때문
            elif distance[node] < d and distance[node] < dist:
                distance[node] = min(dist, d) # ✅ 이전도시 최대 중량과 현재 다리 최대 중량 중 작은 값을 저장
                heapq.heappush(queue, (-distance[node], node))



if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    for i in range(1, n + 1):
        graph[i].sort(reverse=True)
        #print(graph[i])

    distance = [0] * (n + 1)
    start, end = map(int, input().split())

    dijkstra(start, end)



# import sys
#
# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n, m = map(int, input().split())
#     MaxWeight = sys.maxsize
#     graph = [[0] * n for _ in range(n)]
#
#     for _ in range(m):
#         a, b, c = map(int, input().split())
#         if graph[a-1][b-1] == 0:
#             graph[a - 1][b - 1] = c
#             graph[b - 1][a - 1] = c
#         else:
#             graph[a - 1][b - 1] = max(graph[a - 1][b - 1], c)
#             graph[b - 1][a - 1] = max(graph[b - 1][a - 1], c)
#
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if i == j: continue
#                 graph[i][j] = max(min(graph[k][j], graph[i][k]), graph[i][j])
#
#     x, y = map(int, input().split())
#     print(graph[x-1][y-1])


# 3 2
# 1 2 2
# 3 2 5
# 1 3