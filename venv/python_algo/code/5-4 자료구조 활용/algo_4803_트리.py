# 아아아 이것도 유니파인드 문제네 그치?
# 근데 이게 순환 구조면 어떻게 하지??
# 와 이건 내가 너무 생각이 모질랐다
# https://nbalance97.tistory.com/154
# 그냥 단순히 유니파인드 조지고 set에 박아서 나오는 수 갯수만 걍 뽑으면 될 줄 알았는데
# 이러면 사이클이 발생하는 경우(1-2-1)를 거르지 못함
# 그래서 먼저 애들 find 함수 돌려서 나온 부모를 비교해서 같지 않으면 union 하고
# 같으면(사이클 발생) 이니까 사이클 전용 배열에 박아놈
# 여기서 끝내지 않고 그 사이클 배열을 set 에 박아 놓고 for 문을 돌려서 set 없는 부모값을 세는게 답임
import sys

def getFind(a):
    if parent[a] != a:
        parent[a] = getFind(parent[a])
    return parent[a]

def union(a, b):
    a = getFind(a)
    b = getFind(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    input = sys.stdin.readline
    case = 1
    while True:
        n, m = map(int, input().split())
        if n + m == 0: break
        parent = [i for i in range(n+1)]

        cycle = []
        for _ in range(m):
            a, b = map(int, input().split())
            p1, p2 = getFind(a), getFind(b)
            if p1 != p2:
                union(a, b)
            else:
                cycle.append(parent[a])

        group = set()
        for cycle_vertex in cycle:
            group.add(parent[cycle_vertex])

        answer = 0
        for i in range(1, n + 1):
            if parent[i] in group:
                continue
            answer += 1
            group.add(parent[i])

        if answer == 0:
            print("Case %d: No trees." % (case))
        elif answer == 1:
            print("Case %d: There is one tree." % (case))
        else:
            print("Case %d: A forest of %d trees." % (case, answer))
        case += 1

# 6 6
# 1 2
# 2 3
# 1 3
# 4 5
# 5 6
# 6 4
# 0 0

# 5 4
# 1 2
# 2 3
# 3 1
# 4 5
# 0 0