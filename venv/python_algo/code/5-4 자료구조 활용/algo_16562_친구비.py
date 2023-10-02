# 딱봐도 부모노드 묻는 문제 이거 뭐라 하더라 유니파인드 문제
# 근데 젤 최소로 하라자너 그러면 흠
# 하 십 시간 마니 잡아 먹었다 ㅋㅋ
# 설명하자면 틀렸어 그래서 보는데 나랑 진행방식이 차이가 없는거야
# 굳이 따지자면 난 그냥 빠른 순대로 부모를 정했고 그러고 나선 딕셔너리로 최소값을 갱샌해줬을뿐이야
# 한번 할일을 두번 한, 그냥 최적화의 문제지 로직 문제가 아니단 말이야
# 그래서 대체 뭐가 문제지 이러고 있었는데
# set 부분에 박을 때 set에 있는가 없는가 조건절 대상으로 바로 parent[i] 로 박았다는 점이 문제였네 ㅋㅋ (그래서 29%에서 틀림)
# 근데 이게 왜 문제가 되지?? 어차피 받을때 함께 유니온 하면서 정리 되지 않나? 했는데
# 아니지 아니지 정리가 안되지 ㅋㅋㅋ 가령 1-3, 2-3 라고 했을때 사실상 1-2-3 다 같은 부모가 되겠지만
# 자료상 따로해서 2개를 받았으니 만약 cost가 [2, 1, 3] 이라 했을때 1-2-1 형태가 되겠지 이해감?
import sys

def getParent(a:int) -> int:
    if parent[a] != a:
        parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if cost[a] < cost[b]:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())

    cost = [0] + list(map(int, input().split()))
    parent = [i for i in range(0, n+1)]
    friend = set()
    totalCost = 0

    for _ in range(m):
        a, b = map(int, input().split())
        unionParent(a, b)

    for i in range(1, n+1):
        if getParent(i) not in friend:
            totalCost += cost[parent[i]]
            friend.add(parent[i])

    print(totalCost if totalCost <= k else "Oh no")



# 5 3 10
# 10 10 20 20 30
# 1 3
# 2 4
# 5 4

# 5 5 100
# 10 20 30 40 50
# 1 2
# 3 4
# 2 3
# 4 5
# 5 1
# 답 10


# 5 3 20
# 10 20 20 10 30
# 1 3
# 2 4
# 5 4
# 답 20


# 5 4 100
# 1 1 1 1 1
# 1 5
# 2 4
# 4 3
# 5 4