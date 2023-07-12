# 하 존나 멍청하네
# 나는 BFS 로 하나하나 해당 병사들의 값을 구해서 거리값을 배열에 박았는데
# 그럴게 아니라 그냥 전체 거리를 구하고 거기에 병사들 위치만 배열에 박아 넣으면 되는거였어
# 하긴 그게 여러번 계산할꺼를 한번에 계산으로 끝내버리긴해

from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    q.append(destination)
    visited[destination] = 0

    while q:
        now = q.popleft()

        for x in graph[now]:
            if visited[x] == -1:
                visited[x] = visited[now] + 1
                q.append(x)



    return [visited[i] for i in sources]

if __name__ == "__main__":
    n = 3
    roads = [[1, 2], [2, 3]]
    sources = [2, 3]
    destination = 1
    res = [1, 2]

    answer = solution(n, roads, sources, destination)
    print(res == answer, answer)

    n = 5
    roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
    sources = [1, 3, 5]
    destination = 5
    res = [2, -1, 0]

    answer = solution(n, roads, sources, destination)
    print(res == answer, answer)

