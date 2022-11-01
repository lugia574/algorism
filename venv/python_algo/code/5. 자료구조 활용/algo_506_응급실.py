# 응급실은 환자가 도착한 순서대로 진료를 합니다.
# 하지만 위험도가 높은 환자는 빨리 응급조치를 의사가 해야 합니다.

# • 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
# • 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로
#  다시 넣습니다. 그렇지 않으면 진료를 받습니다.

# 즉 대기목록에 자기 보다 위험도가 높은 환자가 없을 때 자신이 진료를 받는 구조입니다.
# 현재 N명의 환자가 대기목록에 있습니다.
# 대기목록상의 M번째는 대기목록의 제일 처음 환자를 0번째로 간주하여 표현한 것입니다.
# ▣ 입력설명
# 첫 줄에 자연수 N(5<=N<=100)과 M(0<=M<N) 주어집니다.
# 두 번째 줄에 접수한 순서대로 환자의 위험도(50<=위험도<=100)가 주어집니다.
# 위험도는 값이 높을 수록 더 위험하다는 뜻입니다. 같은 값의 위험도가 존재할 수 있습니다.
# ▣ 출력설명
# M번째 환자의 몇 번째로 진료받는지 출력하세요.
# ▣ 입력예제 1
# 5 2
# 60 50 70 80 90
# ▣ 출력예제 1
# 3
# ▣ 입력예제 2
# 6 0
# 60 60 90 60 60 60
# ▣ 출력예제 2
# 5
# 큐를 사용해야해
from collections import deque

def emergencyRoom(n,m,arr):
    dq = deque([])
    index = 0
    cnt = 0
    for i in arr:
        if index == m:
            dq.append([i,"t"])
        else:
            dq.append([i,"p"])
        index+= 1

    while True:
        pre = dq.popleft()
        for x, _ in dq:
            if pre[0] < x:
                dq.append(pre)
                pre = []
                break
        if pre :
            cnt += 1
            if pre[1] == "t":
                break

    return cnt

def inputFnc():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    return n, m, arr

N, M, arr = inputFnc()
res = emergencyRoom(N,M,arr)
print(res)

