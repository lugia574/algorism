# 그니까 처음 시작은 1로 잡고 1 >> x 까지의 올라가면서 거리를 구해
# 그 다음은 x >> x2 까지의 공통 부모 찾으며 올라가고 그 거리 더하고
# 계속 이런식으로 반복 하면 되지 않나 싶은데
# https://loosie.tistory.com/622
# 라고 생각했는데 이러면 사실상 쓸데없는 계산을 존나 하는거임
# 각각 정점까지의 값을 distance 배열에 저장하고
# 이게 지금 1761 정점들의 거리 이거 문제랑 같은거거든?
# 그냥 ㄹㅇ 같애 단순히 거리값이 1이냐 특정값이 차이지
# 근데 지금 두 문제 다 이해를 못하고 있음 ㅋㅋ ㅄ ㅋㅋ
# 아니 더 나아가 LCA2 문제 부터 왜 이렇게 되는지를 잘 몰라 ㅋㅋㅋ
# 하나하나 뜯어보면서 아 이게 이렇게 올라가는건가 이거 자체를 몰라 ㅋㅋㅋ

import sys, math
sys.setrecursionlimit(int(1e9))

def depthCheck(cur, d, p):
    depth[cur] = d
    check[cur] = True

    if cur != 1:
        distance[cur] += distance[p] + 1

    for next in graph[cur]:
        if check[next]: continue
        parent[next][0] = cur
        depthCheck(next, d + 1, cur)

def setParent():
    depthCheck(1, 0, 0)

    for i in range(1, LOG):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    # b가 더 깊도록 설정
    if depth[a] > depth[b]:
        a,b = b,a
        # 더 깊은 b에 대해 동일해질때까지 올린다.

    for i in range(LOG-1,-1,-1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]

    if a==b:
        return a

    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상.
    return parent[a][0]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    LOG = int(math.ceil(math.log(N) / math.log(2))) + 1
    distance = [0] * (N + 1)
    parent = [[0] * LOG for _ in range(N+1)]
    check = [0] * (N + 1)  # 깊이가 계산 되었는지 여부
    depth = [0] * (N + 1)

    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    setParent()

    M = int(input())
    arr = [int(input()) for _ in range(M)]
    res = 0

    for i in range(1, M):
        start = arr[i-1]
        end = arr[i]
        res += distance[start] + distance[end] - 2 * distance[lca(start, end)]

    print(res)