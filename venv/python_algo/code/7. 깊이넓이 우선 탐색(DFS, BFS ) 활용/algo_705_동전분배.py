# 동전 분배하기(DFS)
# N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다.
# 세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 총액이 가장 큰
# 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
# 단 세 사람의 총액은 서로 달라야 합니다.
# ▣ 입력설명
# 첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다.
# 그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.
# ▣ 출력설명
# 총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.
# ▣ 입력예제 1
# 7
# 8
# 9
# 11
# 12
# 23
# 15
# 17
# ▣ 출력예제 1
# 5
# 해설 : 29(12+17), 32(8+9+15), 34(11+23) 로 분배하면 최대금액과 최소금액의 차가 5가 되어 5가 최소차가 된다.

def division(l, a, b, c):
    global res
    global maxScore

    if maxScore < max(a, b, c):
        return

    if l == n:
        if a != 0 and b != 0 and c != 0 and a != b and c != b and a != c:
            maxNum = max(a, b, c)
            minNum = min(a, b, c)
            gap = maxNum-minNum
            if gap < res:
                res = gap
                maxScore = maxNum

    else:
        division(l+1, a + coinArr[l], b, c)
        division(l+1, a, b + coinArr[l], c)
        division(l+1, a, b, c + coinArr[l])

def solution(l):
    global res
    if l == n:
        gap = max(people) - min(people)
        if gap < res:
            tmp = set()
            for i in people:
                tmp.add(i)
            if len(tmp) == 3:
                res = gap
    else:
        for i in range(3):
            people[i] += coinArr[l]
            solution(l + 1)
            people[i] -= coinArr[l]
if __name__ == "__main__":
    n = int(input())
    coinArr = []
    for _ in range(n):
        coinArr.append(int(input()))

    res = 2147000000
    maxScore = 2147000000
    people = [0] * 3
    division(0,0,0,0)
    solution(0)
    print(res)
