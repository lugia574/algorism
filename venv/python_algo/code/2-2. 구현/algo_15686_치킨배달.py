# === 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 흠 m 으로 몇개를 빼냐 이게 문제인거 같은데
# 이게 막말로 50 * 50 치킨집중 2개를 조합해라 이러면 으마으마한거 같은데?
# 라고 해서 무슨 combinations을 갈겨야하나? 존나 싫은데
# 이렇게 생각했는데 사실 컴비네이션 이거 백트레킹으로도 충분히 구현 쌉가능이자너?
# 그냥 단순하게 조합을 해서 연산을 했을때 시초가 되냐 안되냐만 따지면 되는거다 이말이야

import sys, heapq

def check():
    distance = 0
    for hx, hy in house:
        dist = sys.maxsize
        for e, cx, cy in chickenSet:
            dist = min(dist, abs(hx - cx) + abs(hy - cy))
        distance += dist

    heapq.heappush(res, distance)

def backTracking(level):
    if level == m:
        check()
        return
    for idx, loc in enumerate(chicken):
        x, y = loc
        if visited[x][y]: continue
        if chickenSet and idx < chickenSet[-1][0]: continue # 시간단축, 오름차순

        visited[x][y] = True
        chickenSet.append((idx, x, y))
        backTracking(level+1)
        visited[x][y] = False
        chickenSet.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    house = []
    chicken = []
    visited = [[False] * n for _ in range(n)]

    chickenSet = []
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                house.append((i, j))
            elif board[i][j] == 2:
                chicken.append((i, j))
    backTracking(0)

    print(heapq.heappop(res))