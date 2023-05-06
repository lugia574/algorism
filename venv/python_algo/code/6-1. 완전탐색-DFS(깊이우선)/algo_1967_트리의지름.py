# 아무리 생각해도 그냥 무식하게 쳐 DFS 를 돌렸다가는 무조건 시초 뜨고 뻗어 버릴꺼 같은데
# 해결법은 가지치기를 잘하던가 >> 근데 이거 나 자신 없음
# 아니면 결국 보면 중복되는 처리들이 많음 1 >> 7 까지 가냐 1 >> 8 까지 가냐의 값이 상당부분 같음
# 이를 이용해서 어떻게 dp 를 할 수 있지 않을까??? 아이디어만 이렇게 되네?
# 이러면 우선 1부터 DFS 로 들어가면서 값을 갱신 해줘야하나??
####
# https://kyun2da.github.io/2021/05/04/tree's_diameter/
# 트리에서 아무 노드나 잡고 그 노드에 대한 가장 먼 노드를 구하고 이 노드를 n1이라고 하자.
# n1 에대한 가장 먼 노드를 한번 더 구한다. 이 노드를 n2라고 하자.
# 이제 n1과 n2의 거리가 트리의 지름이 된다.
# 띠요요옹?
# 원리 증명 https://koosaga.com/14

import sys
sys.setrecursionlimit(10**9)
def dfs(node, wei):
    for x in graph[node]:
        a, b = x
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n+1)]

    for i in range(n-1):
        a, b, cost = map(int, input().split())
        graph[a].append([b, cost])
        graph[b].append([a, cost])
    distance = [-1] * (n + 1)
    distance[1] = 0
    dfs(1, 0)

    start = distance.index(max(distance))
    distance = [-1] * (n + 1)
    distance[start] = 0
    dfs(start, 0)
    print(max(distance))