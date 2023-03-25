# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.
#
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 1. 아이디어
# DFS 와 BFS 로 풀어야지 그치?
# 각각 두개의 메소드를 만들어서 실행 시키고 그에 대한 결과값 리스트를 받아서 쏘면 될듯
# 우선 정렬을 해야할꺼 같기도 하고 흠흠 그래프를 어떻게 해야하지? 무조건 1부터 시작하는게 아니라 정렬이 좀 애매한데
# 그냥 없이 쭉 for 문 만들어서 돌려야하나?
# 각 check 리스트를 가지고

# 2. 시간
#

import sys
from collections import deque

def DFS(v):
    visited[v] = 1
    dfs.append(v)
    for i in node[v]:
        if (visited[i] == 0):
            DFS(i)

def BFS(v):
    visited[v] = 1
    bfs.append(v)
    queue = [v]

    while(queue):
        for i in node[queue.pop(0)]:
            if(visited[i] == 0):
                visited[i]=1
                bfs.append(i)
                queue.append(i)

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    node = [[]for _ in range(n + 1)]
    visited = [0] * (n + 1)
    dfs = []
    bfs = []

    for i in range(m):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

    for j in range(n + 1):
        node[j].sort()
        print(node[j])

    DFS(v)
    for j in range(n+1):
        visited[j]= 0
    BFS(v)

    for order in dfs:
        print(order, end=" ")
    print()
    for order in bfs:
        print(order, end=" ")

