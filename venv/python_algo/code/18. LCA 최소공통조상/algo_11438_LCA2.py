# 기존 방식에서 조금더 효율적으로 처리 하는 방법은
# dp 를 이용해 2^i 급으로 거슬러 올라가는거임
# 세그먼트 트리를 이용해도 됨
# 매 쿼리마다 거슬러 M logN 의 복잡도를 가짐


# 1 << i는 비트 시프트 연산자인 비트 왼쪽 시프트(<<)를 사용하여 1을 i번만큼 왼쪽으로 이동시킵니다.
# << 연산자는 주어진 수를 이진수로 표현했을 때, 각 비트를 왼쪽으로 지정된 횟수(i)만큼 이동시키는 연산입니다. 이동된 비트는 왼쪽에서 0으로 채워집니다.
# 예를 들어, i가 2인 경우 1 << 2는 1을 이진수로 표현했을 때 왼쪽으로 2번 이동하므로 결과는 4가 됩니다.
# 이는 이진수 0001을 왼쪽으로 2번 이동하여 0100를 얻은 것과 같습니다.
# 즉, 1 << i는 2의 i제곱을 의미합니다.
# 이를 활용하여 위의 코드에서는 2^i만큼의 깊이 차이를 나타내는 연산을 수행하고 있습니다.

# 라고 한다
import sys
sys.setrecursionlimit(int(1e9))

def depthCheck(x, d):
    check[x] = True
    depth[x] = d

    for y in graph[x]:
        if check[y]: continue
        parent[y][0] = x # 자기 바로 윗 부모는 바로 적어주는거
        depthCheck(y, d+1)

def setParent():
    depthCheck(1, 0)

    # dp 로 제곱급으로 올라가면서 부모를 찾음
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    # b 가 더 깊도록 스압
    if depth[a] > depth[b]:
        a, b = b, a

    # 깊이가 동일하도록
    for i in range(LOG -1, -1 , -1):
        # 2^i 만큼 깊이차이가 충분하다면
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a
    for i in range(LOG - 1 , -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]
if __name__ == "__main__":
    input = sys.stdin.readline
    LOG = 21
    n = int(input())

    parent = [[0] * LOG for _ in range(n+1)]
    depth = [0] * (n+1)
    check = [0] * (n+1)

    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    setParent()

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        print(lca(a, b))



