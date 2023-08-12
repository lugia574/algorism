import sys
sys.setrecursionlimit(int(1e9))

def dfs(graph, v, visted):
    # 함수 밖에 cnt값을 쓰기 위해서 global이라고 명시
    global cnt
    # 방문할 때마다 순차 값 변경
    visted[v] = cnt
    # 연결된 노드 방문
    for i in graph[v]:
        # 방문 안한 노드일 경우
        if visted[i] == 0:
            # 순차 증가
            cnt += 1
            # dfs 실행
            dfs(graph, i, visted)


if __name__ == "__main__":
    n, m, r = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    visted = [0] * (n + 1)
    cnt = 1

    # 연결된 노드 입력 받기
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # 오름차순 정리
    for i in range(n + 1):
        graph[i].sort()

    dfs(graph, r, visted)
    # 순차 출력
    for i in range(n + 1):
        if i != 0:
            print(visted[i])