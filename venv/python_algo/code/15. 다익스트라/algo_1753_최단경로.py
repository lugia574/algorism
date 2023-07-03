# 내가 푼 방식은 플루로이드 워샬 알고리즘 방식으로
# 이렇게 하니까 메모리 초과가 되버리네~
# 다익스트라 알고리즘은 하나의 정점에서 나머지 모든 정점까지의 최단 거리를 찾는 알고리즘이다.
# 모든 정점의 최단거리를 구하는 플로이드-워셜 알고리즘과 다른 알고리즘이니 착각하지 말자!
# 라네~

# https://www.youtube.com/watch?v=611B-9zk2o4&t=472s
import sys
import heapq


def Dijkstra(start):
    # 가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    # 힙에 원소가 없을 때 까지 반복.
    while heap:
        wei, now = heapq.heappop(heap)

        # 현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            # 현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치(next_wei)
            next_wei = w + wei
            # 다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
            if next_wei < dp[next_node]:
                # 계산했던 next_wei를 가중치 테이블에 업데이트.
                dp[next_node] = next_wei
                # 다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
                heapq.heappush(heap, (next_wei, next_node))

if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    V, E = map(int, input().split())
    #시작점 K
    K = int(input())
    #가중치 테이블 dp
    dp = [INF]*(V+1)
    heap = []
    graph = [[] for _ in range(V + 1)]

    #초기화
    for _ in range(E):
        u, v, w = map(int, input().split())
        #(가중치, 목적지 노드) 형태로 저장
        graph[u].append((w, v))


    Dijkstra(K)
    for i in range(1,V+1):
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