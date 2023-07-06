# 우주신 ㅇㅈㄹ
# 별거 아닌데 좀 설명이 불친절해서 이해를 못했었음
# https://steady-coding.tistory.com/1201
# https://velog.io/@jini_eun/백준-1774번-우주신과의-교감-Java-Python
#
import sys

def getParent(a):
    if parent[a] != a:
        parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 거리계산 a^2 + b^2 = c^2 이 피타고라스
def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    point = [] # 좌표
    parent = [i for i in range(N + 1)]
    edges = []
    result = 0

    for _ in range(N):
        x, y = map(int, input().split())
        point.append((x, y))

    for _ in range(M):
        x, y = map(int, input().split())
        unionParent(x - 1, y - 1)

    # 모든 point 간에 간선, 비용 계산 저장
    for i in range(N - 1):
        for j in range(i + 1, N):
            edges.append((dist(point[i], point[j]), i, j))
    
    # 거리가 낮은 순으로 정렬
    edges.sort(key=lambda x: x[0])

    # 거리가 낮은 순으로 정렬된거에 Parent 가 다른 애들끼리 union ㄱㄱ
    for e in edges:
        cost, x, y = e
        if getParent(x) != getParent(y):
            unionParent(x, y)
            result += cost

    print('%.2f' % (result))
