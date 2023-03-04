# 침몰하는 타이타닉(그리디)
# N명이 있습니다. 구명보트를 타고 탈출해야 하는데 구명보트는 2명 이하로만 탈 수 있으며,
# 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
# N명이 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.

# ▣ 입력설명
# 첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
# 두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다.
# 각 승객의 몸무게는 M을 넘지는 않습니다. 즉 탈출을 못하는 경우는 없습니다.

# ▣ 출력설명
# 첫째 줄에 구명보트의 최소 개수를 출력합니다.

# ▣ 입력예제 1
# 5 140
# 90 50 70 100 60
# ▣ 출력예제 1
# 3

# 50 60 70 90 100 // 140
from collections import deque

# deque 를 사용하면 훨씬 효율적으로 할 수 있음
# 일반적인 list 는 pop 을 할 시 나머지 요소들이 다 앞으로 땡겨지는 연산을 하는데
# deque 는 약간 linked list랑 비슷한듯? 아닌가??
# https://www.leafcats.com/125 여기에 있긴함
def solution(m,p):
    p = deque(p)
    cnt = 0
    while p:
        if len(p)== 1:
            cnt += 1
            break
        if p[0]+ p[-1] > m:
            p.pop()
            cnt += 1
        else:
            p.popleft()
            p.pop()
            cnt+=1
    return cnt


def titanicSurvive(m,p):
    cnt = 0

    while len(p) > 1:
        minW = p[0]
        maxW = p[-1]
        # p[len(p)-1]

        if minW + maxW <= m:
            cnt += 1
            p.pop(0)
            p.pop()
        else:
            cnt += 1
            p.pop()

    if len(p) == 1:
        cnt += 1

    return cnt

def inputFnc ():
    N, M = map(int, input().split())
    passenger = list(map(int,input().split()))

    return N,M,passenger

N,M,passenger = inputFnc()
passenger.sort()
res = titanicSurvive(M,passenger)
print(res)