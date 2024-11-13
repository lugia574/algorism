# 이게 말이지 k 번째 최단 경로랑 비슷하고 생각하는데
# 이거는 엄밀히 말하면 2번째 최단 경로 아님? 띠이이용 맞는거 같은데?
# 딱히 몇번째 최단경로의 루트를 말해라도 아니고 단순 길이만 내는거면 그냥 쌉 k번째 최단경로 맞제
# 아아아 그러네 이게 최단경로가 여러개면 차지해버리네 그러면 조건문을 하다 더 줘야할듯
# 띠용 엄연히 2번째 경로값이 있는데 왜 없다고 -1 해버리냐??
# 왜 -1 하녀면 엄연히 말해선 최단경로 루트가 아니니까? 이지 않을까
# 갈수 있는 루트가 2갠데 첫번째꺼는 최소경로라면 나머진 거의 최단 이라고 부르기에는 좀 그러자너 안그럼?
# 개소리고 걍 답 보자 ㅋ
# https://jjangsungwon.tistory.com/98
# 와 ㅅㅂ 이건 생각 못했네 k번째 최단 경로랑 다르네 ㅋㅋ
# 이거 이건 내가 직접 짜봐야함 ㅇㅇㅇ
# 브리핑을 해보도록 할께요
# 자 우선 가장 핵심을 먼저 알아둬야해요 이걸 못알아먹으면 이 문제를 풀 수가 없어요
# 거의 최단 경로란 최단 경로에 포함되지 않는 도로로만 이루어진 경로 중 가장 짧은 것을 말한다.
# 즉 최단경로를 제외한 경로들에서 최단 경로를 찾아라 라는 소리임 이걸 못알아먹어서 단순히 k 번째 최단 경로랑 같다고 생각한게 문제였음
# 그럼 이제 풀이 방법을 읊어봄
# 1. 최단경로를 먼저 구함
# 2. 최단경로에 나온 최솟값을 토대로 BFS 를 돌려서 최솟값에 해당되는 최단경로 루트들을 모음
# 3. 해당 최단경로 루트들을 지우고 나서 다시 최단경로를 구함 >> 거의 최단경로

# 여기서 또 내가 생각 못한 문제가 발생을 하네
# 경로를 추적하기 위해서 역순 저장을 따로 해야함
# 그리고 기존 graph 방식을 단순 2차배열이 아닌 딕셔너리 형태로 해야지
# 루트 삭제에 용이하겠지
# 이걸 생각을 못해서 헤맸어 또 또 도 어렵다~ 어려워
import sys, heapq
from collections import deque

def dijkstra():
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0  # 출발지

    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인하면서 거리 업데이트
        for i in graph[now]:
            cost = dist + graph[now][i]
            if cost < distance[i]:  # 해당 지점을 거치는 것이 거리가 짧은 경우
                distance[i] = cost
                heapq.heappush(q, (cost, i))


def bfs():
    q = deque()
    q.append(d)
    while q:
        v = q.popleft()
        if v == s:  # 시작점 도달
            continue  # break하면 다른 최단 경로를 확인할 수 없다.
        for pre_v, pre_c in r_graph[v]:
            if distance[pre_v] + graph[pre_v][v] == distance[v]:
                if (pre_v, v) not in remove_List:
                    remove_List.append((pre_v, v))
                    q.append(pre_v)


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:  # n과 m이 0이면 종료
            break
        s, d = map(int, sys.stdin.readline().split())  # 출발지, 도착지
        graph = [dict() for _ in range(n)]
        r_graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, sys.stdin.readline().split())  # 도로 정보 입력
            graph[u][v] = p
            r_graph[v].append((u, p))  # 경로를 추적하기 위해서 역순 저장

        # 다익스트라 알고리즘을 사용하여 최단 거리 찾기
        distance = [INF] * n
        dijkstra()

        # BFS를 사용하여 최단 경로 추적
        remove_List = list()
        bfs()

        # 최단 경로 제거
        for u, v in remove_List:
            del graph[u][v]

        # 다익스트라 알고리즘을 사용하여 최종 최단 경로 찾기
        distance = [INF] * n
        dijkstra()
        if distance[d] == INF:  # 거의 최단 경로가 없는 경우
            print(-1)
        else:
            print(distance[d])

# 4 6
# 0 2
# 0 1 1
# 1 2 1
# 1 3 1
# 3 2 1
# 2 0 3
# 3 0 2
# 0 0

