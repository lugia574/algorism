# https://konkukcodekat.tistory.com/entry/%EB%B0%B1%EC%A4%80-1167-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%80%EB%A6%84-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-BFS-%ED%92%80%EC%9D%B4
# 못푸는거 실화?
# 이거 무조건 풀수 있어야하는 문젠데 실화냐?
# 1번 노드를 탐색해서 가장 거리가 길게 나온 노드를 저장하고, 그 노드를 또 탐색해서 가장 길이가 나온 케이스를 출력하면 됩니다. 라고 하데
# 나는 하나하나 노드 하나씩 dfs 돌리면서 했는데
# 당연히 시초 떳고 방법은 루트노드로 하나 돌고 거기서 나온 최고거리로 하나 또 돌면 된다고 하네
import sys
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start]=True
    while len(queue)!=0:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i[0]] == False:
                queue.append(i[0])
                visited[i[0]]=True
                distance[i[0]]= distance[node]+i[1]


if __name__ == "__main__":
    input = sys.stdin.readline
    v = int(input())
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v + 1)
    distance = [0] * (v + 1)
    for _ in range(v):
        path = list(map(int, sys.stdin.readline().split()))

        # 각 입력 Line의 정보를 받아 Parsing 후 node_graph에 연결 정보 저장
        path_len = len(path)
        for i in range(1, path_len // 2):
            graph[path[0]].append([path[2 * i - 1], path[2 * i]])

    bfs(1)
    result_index = distance.index(max(distance))
    visited = [False] * (v + 1)
    distance = [0] * (v + 1)
    bfs(result_index)
    print(max(distance))
