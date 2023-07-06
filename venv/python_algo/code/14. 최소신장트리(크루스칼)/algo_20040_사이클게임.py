# 아 이거 별거 아닌데
# 내가 멍청해서 이해를 못했음 이 문제는 그림으로 띡띡 그려볼떄 이해를 팍 했어야하는데
# 그걸 이해 못해가지고 시간 잡아 먹음
# 이게 지금 분류상으로 들어가서 union 쓴다는걸 아니까 그나마 빨리 푼거지
# 만약에 모른 상태에 던져졌다? BFS로 해야하나 어쩌나 개고생했을꺼임
# 보나마나 BFS 로 했음 시초 걸리고 디졌음

# 직접 그려보면 됨 예제 2번을 보자
# 0 - 1 은 각각 자기자신인 0 1 을 가리키고 있는 상태에서 둘을 이음 그럼 0 0 이 되겠지
# 1 - 2 는 0 2 상태고 이으면 0 0
# 1 - 3 는 0 3 상태 이으면 0 0
# 0 - 3 은 0 0 상태 즉 이미 같은 부모를 가진 상태에서 이어진다는거임 그럼 이때가 cycle 이 완성되는 거
# 이걸 눈치 못채서 끙끙대고 있었음

import sys

def getParent(a):
    if a != parent[a]:
        parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b):
    global cnt
    a = getParent(a)
    b = getParent(b)
    ans = False
    if a == b:
        ans = True

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return ans
if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    cnt = 0
    parent = [i for i in range(n)]

    for i in range(m):
        a, b = map(int, input().split())
        end = unionParent(a, b)
        if end:
            print(i+1)
            break

    if not end:
        print(0)