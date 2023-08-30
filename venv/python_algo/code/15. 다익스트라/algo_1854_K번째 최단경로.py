# 참내 그냥 최단경로도 아니고
# k 번째로 빠른 최단 경로란다 참참참내내내
# 먼가 출력도 난해한데
# 대충 최단 경로 문제에서 한번 꼰거 아님?
# 그러면 다익스트라로 풀어서 그중에 k 번째 얘를 뽑으면 되는거 아닌가?
# https://velog.io/@hamfan524/백준-1854번-Python-파이썬-Dijkstra
# 나랑 접근 방식이 비슷함
# 차이점은 난 다익스트라 알고를 제대로 쓸줄 모른다는거고 재는 잘쓴다는거지 ㅋ
# 또또 이런다 ㅋㅋㅋ 또 시작이야 ㅋㅋㅋㅋㅋ 머저리야 머저리 에휴 ㅋ

import sys, heapq

def dijkstra(start):
    heapq.heappush(heap, [start, 0])
    dp[start][0] = 0
    while heap:
        now, l = heapq.heappop(heap)
        for nextNode, nextLen in graph[now]:
            nextLen += l
            if nextLen < dp[nextNode][k-1]:
                dp[nextNode][k-1] = nextLen
                dp[nextNode].sort()
                heapq.heappush(heap, (nextNode, nextLen))


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize

    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dp = [[INF] * k for _ in range(n+1)]
    heap = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(1)

    #print(dp)
    for i in range(1, n+1):
        if dp[i][k-1] == INF: print(-1)
        else: print(dp[i][k-1])
