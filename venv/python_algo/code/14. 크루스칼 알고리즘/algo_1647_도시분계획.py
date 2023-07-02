# 이것도 크루스칼인데 좀더 심화이긴하네
# 근데 별거 없음
# 그냥 다 하나씩 연결한다음에 가장 높은값 하나 때버리면 되는듯???
# 띠용 sum으로 연산 자르기 한게 오히려 연산을 늘리고 있었음

import sys

def getParent(a):
    if a == parent[a]:
        return a
    parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    routes = [list(map(int, input().split())) for _ in range(m)]
    routes.sort(key=lambda x: x[2])  # 비용을 기준으로 정렬

    maxCost = 0  # 최대 비용
    totalCost = 0  # 총 비용

    for a, b, c in routes:
        if getParent(a) != getParent(b):
            unionParent(a, b)
            totalCost += c
            maxCost = max(maxCost, c)

    # 분리된 마을을 다시 합치기 위해 최대 비용을 제거
    totalCost -= maxCost

    print(totalCost)
