# 오늘부터 N+1일째 되는 날 휴가를 가기 위해서, 남은 N일 동안 최대한 많은 상담을 하고 떠나려 한다.
# 각각의 상담은 상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P
# 만약 N = 7이고, 아래와 같이 예약이 잡혔있다면
# 1일 2일 3일 4일 5일 6일 7일
# T 4 2 3 3 2 2 1
# P 20 10 15 20 30 20 10
# 1일에 잡혀있는 상담은 총 4일이 걸리며, 상담했을 때 받을 수 있는 금액은 20이다. 만약 1일에 예약된 상담을 하면 4일까지는 상담을 할 수가 없다.
# 상담의 최대 이익은 1일, 5일, 7일에 있는 상담을 하는 것이며,
# 이때의 이익은 20+30+10=60이다.
# 최대 수익을 구하는 프로그램을 작성하시오.
# ▣ 입력설명
# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
# 둘째 줄부터 1일부터 N일까지 순서대로 주어진다. (1 ≤ T ≤ 7, 1 ≤ P ≤ 100)
# ▣ 출력설명
# 첫째 줄에 현수가 얻을 수 있는 최대 이익을 출력한다.
# ▣ 입력예제 1
# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10
# ▣ 출력예제 1
# 60
def consultingDFS (l,st, sp):
    global maxPay
    if l > n:
        return
    if l == n:
        if sp > maxPay:
            maxPay = sp
    else:
        consultingDFS(l+ct[l], st+ct[l], sp+cp[l])
        consultingDFS(l+1, st, sp)

if __name__ == "__main__":
    n = int(input())
    ct = []
    cp = []

    for _ in range(n):
        t, p = map(int,input().split())
        ct.append(t)
        cp.append(p)
    check = [0] * n
    maxPay = -21467000000
    consultingDFS(0,0,0)
    print(maxPay)
