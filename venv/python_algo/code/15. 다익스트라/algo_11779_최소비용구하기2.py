# 띠요요옹 먼가 최소비용이 같은데 이상하다~
# 이런 ㅅㅂ 이미 푼건데 시간낭비 했네
# 이게 테케를 보면 답이 2개야 1-3-5, 1-4-5 이렇게 두개가 최소비용인데
# 답은 1-3-5 하나여 답이 복수일땐 어떻게 해라라고 나오지도 않았고
# 아니 그래서 뭐 정렬했을때 앞에 오는 순인가 해서 했는데 틀려서 먼가 막 찾아봤더니
# 스폐셜 저지라고 상관없데~~~~ 십사비 ㅏㅇㅇ 뭐여 이게
import sys, heapq

def dijkstra(start):
    hq = []
    heapq.heappush(hq, [0, start, [start]])
    while hq:
        weight, now, g = heapq.heappop(hq)
        if now == end:
            return g
        if dp[now] < weight: continue

        for nextNode, newWeight in graph[now]:
            newWeight += weight
            if dp[nextNode] > newWeight:
                dp[nextNode] = newWeight
                heapq.heappush(hq, [newWeight, nextNode, [*g, nextNode]])

if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    start, end = map(int, input().split())
    dp = [INF] * (n+1)
    dp[start] = 0

    res = dijkstra(start)
    print(dp[end])
    print(len(res))
    print(*res)