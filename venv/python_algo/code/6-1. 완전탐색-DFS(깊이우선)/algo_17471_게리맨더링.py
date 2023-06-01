# https://velog.io/@study-dev347/백준-17471-게리맨더링
# https://velog.io/@bobae1998/백준-17471-게리맨더링-JAVA
# 대충 나는 BFS 로 하나씩 먹은 다음에 이것을 먹었을때 나머지는 싹다 반대쪽 구역이라고 했을때
# 올바른 구역형성인지 판단하고 맞으면 2 구역의 인구수 차이를 구해서 값을 비교 갱신해준다라고 아이디어를 짯는데
# 어떻게 구역을 짜고, 그게 올바른 구역인지 판단하는게 너무 으렵더라

# 자 어떻게 접근해야하는지 순서를 말해보면
# 1. 1~N까지 구역을 2개의 선거구로 나눠주기 (부분집합)
# 2. 나눠준 선거구 내에서 구역들이 전부 연결되었는지 확인 (그래프 탐색 - BFS)
# 3. 전부 연결되어 있으면 인구차 구하기
# 나는 12 를 함께 해버릴라 했어~ 힘들지~

# 2개의 선거구로 나눠주는 것은 부분집합 구할 때 처럼 구할 수 있다.
#
# 나눠준 선거구 내에서 구역들이 전부 연결되었는지는 A선거구에 속하는 지역 하나를 뽑아서 그래프 탐색을 실시,
# B 선거구에 속하는 지역 하나를 뽑아서 그래프 탐색을 실시 후 각 그래프 탐색의 방문 결과가 선거구 분리 결과와 같은지 비교한다.
#
# 선거구 내의 지역들이 전부 연결되었으면, 각 선거구 별 인구차를 나눠준다.

# 라고 하네?

import sys
from collections import deque
from itertools import combinations


def is_connected(nodes):
    q = deque()
    check = [False for _ in range(n)]
    q.append(nodes[0])
    check[nodes[0]] = True

    while q:
        node = q.popleft()

        for i in range(len(arr[node])):
            if arr[node][i] == 0: continue
            if i not in nodes: continue
            if not check[i]:
                check[i] = True
                q.append(i)

    return check.count(True) == len(nodes)


def get_total(nodes):
    total = 0
    for node in nodes:
        total += people[node]

    return total


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    people = list(map(int, input().rstrip().rsplit()))

    arr = [[0 for _ in range(n)] for _ in range(n + 1)]

    for i in range(n):
        _, *dsts = map(int, sys.stdin.readline().rstrip().split())
        for dst in dsts:
            arr[i][dst - 1] = 1

    cases = []
    X = {i for i in range(n)}
    # INF = int(1e9)
    INF = 1001
    ans = INF

    for i in range(1, n // 2 + 1):
        As = tuple(combinations(X, i))
        for A in As:
            B = list(X.difference(A))

            if is_connected(A) and is_connected(B):
                a_total = get_total(A)
                b_total = get_total(B)
                ans = min(ans, abs(a_total - b_total))

    print(-1 if ans == INF else ans)
