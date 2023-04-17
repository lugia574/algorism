# 단순히 원을 피해가는 거면 모를까
# 최소환으로 거쳐가는 경로를 짜라고?
# 이걸 어떻게 짬?
# 괜히 기하학이 아니네 기괴하구만
# 라고 생각했는데 찾아보니까 그냥 딱 거쳐갈 것들만 체크하면 된다~
# 그러니까 각 출발점과 도착점이 포함된 원만 체크하면 된다
# 만약에 출발점, 도착점 모두를 포함할 수 있음 존나존나 큰 원이니까 체크 안됨

# 임의의 좌표가 원의 범위 안에 포함 되는지 안되는지 체크하는 법
# (반지름^2) > (((원의 중심 좌표 X - 임의의 좌표 TX) ^ 2) + ((원의 중심 좌표 Y - 임의의 좌표 TY) ^ 2)))

import sys

def fnc():
    startX, startY, endX, endY = list(map(int, input().rsplit()))
    n = int(input())
    cnt = 0
    for _ in range(n):
        px, py, r = map(int, input().rsplit())
        b1 = True if r ** 2 > (((px - startX) ** 2) + ((py - startY) ** 2)) else False
        b2 = True if r ** 2 > (((px - endX) ** 2) + ((py - endY) ** 2)) else False
        if (b1 or b2) and b1 != b2:
            cnt += 1
    return cnt

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        res = fnc()
        print(res)