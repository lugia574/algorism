# 오늘도 알고리즘 놀이 존나가 귀찮아요~ 그냥 놀고 시퍼여~
# 먼가 표현 방식이 좀 다르지 결국 내용은 똑같은거 같긴한데
# 먼가 살짝 어려운데 이게 정답 비율 53 이라고?
# 아하 뭐가 문제인지 알겠네
# 핵심은 주어진 값만 길이 있는게 아니라 지름길을 안가고 일반적인 길로 가는것 역시 길이라는 소리임
# 그러니까 1 > 2, 2 > 3, 3 > 4 이렇게 일반적으로 가는 길로 우선 싹 graph 를 만들어 놓고
# 거기에 주어진 값을 얹어서 graph 를 만들고 그걸 다익스트라 돌리면 된다 이거야 여기서 만들때 if e > d: 같은 예외 값들은 제외 시키면 되고

import heapq, sys

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        #지금 힙큐에서 뺀게 now까지 가는데 최소비용이 아닐수도 있으니 체크
        if dist > distance[now]:
            continue

        for newDist, nextNode in graph[now]:
            cost = dist + newDist
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q,(cost, nextNode))


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)
    n, d = map(int,input().split())
    graph = [[] for _ in range(d+1)]
    distance = [INF] * (d+1)

    #일단 거리 1로 초기화.
    for i in range(d):
        graph[i].append((1, i + 1))

    #지름길 있는 경우에 업데이트
    for _ in range(n):
        s, e, l = map(int,input().split())
        if e > d:# 고려 안해도 됨.
            continue
        graph[s].append((l, e))

    dijkstra(0)
    print(distance[d])


# 5 15
# 0 5 1
# 0 5 2
# 5 10 1
# 10 16 1
# 11 14 9