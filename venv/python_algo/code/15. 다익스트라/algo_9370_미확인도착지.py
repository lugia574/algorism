# 문제가 좀 난해하긴한데
# 보니까 결국 스타트 지점인 s 가 있고
# g, h 두개의 지점이 있는게 딱
# 저번 문제의 특정한 최단경로 문제랑 같은 문제인듯?
# s - g - h
# s - h - g 두개의 경로중 뭐가 더 최단이냐 가리고 그 값에서
# 목적지 후보 값들 중 젤 낮은 게 정답이라는 소리 아닌가?
# 내가 문제를 잘못 이해한듯?? 왜 답이 2개로 나옴?
# 답지를 보는데 왜 출발지에서 바로 출발한 값이랑 비교를 하냐?

# ㅅㅂ 어렵네 글 이해하기 어렵네 ㅋㅋ
# 목적지까지 우회하지 않고 최단거리로 갈 것이라 확신한다 이걸 잘 봐야함
# 그리고 예제의 test 1 을 보면 각이 나옴
# 1 - 2 - 3 - 4
#           - 5    이런식으로 구성되어 있음 3번에서 4번, 5번으로 갈림길이 나온거임
# 이때 4번이 더 가깝냐 5번이 더 가깝냐 이런건 의미 없음 이유는
# 4번으로 가든 5번으로 가든 최단거리로 루트이기 때문에

# 그렇기에 단순히 경로를 비교해서 제일 작은 값을 출력하는게 아니라
# 출발지점에서 바로 목적지 후보로 가는 최단 루트와  g, h 를 거쳐가는 루트가 같은 코스트 인것들을 답에 박아 넣는거임

import sys
import heapq

def dijkstra(start):
    ditance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (start, 0))
    ditance[start] = 0
    while q:
        now, dist = q.pop()
        if ditance[now] < dist:
            continue
        for nextNode, nextDist in graph[now]:
            nextDist += dist
            if ditance[nextNode] > nextDist:
                ditance[nextNode] = nextDist
                heapq.heappush(q, (nextNode, nextDist))

    return ditance

if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    for _ in range(int(input())):
        n, m, t = map(int, input().split()) # 노드, 간선, 목적지 후보
        s, g, h = map(int, input().split()) # 시작점, 중간 경유지1, 2
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append([b, c])
            graph[b].append([a, c])

        goalList = [int(input()) for _ in range(t)] # 목적지 후보 Arr

        originRoute = dijkstra(s)
        gRoute = dijkstra(g)
        hRoute = dijkstra(h)

        routeA = originRoute[g] + gRoute[h]
        routeB = originRoute[h] + hRoute[g]
        answer = []

        for x in goalList:
            if originRoute[x] == routeA + hRoute[x] or originRoute[x] == routeB + gRoute[x]:
                answer.append(x)

        answer.sort()
        print(*answer)


# 1
# 5 4 2
# 1 2 3
# 1 2 6
# 2 3 2
# 3 4 4
# 3 5 3
# 5
# 4