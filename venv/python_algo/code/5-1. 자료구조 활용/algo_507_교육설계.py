# 교육과정 설계
# 요약하면 필수 과목을 주어주고
# 해당 과목 순서는 맞게 배열한 리스트는 yes 하고 아닌 것은 no 하래
# ▣ 입력설명
# 첫 줄에 한 줄에 필수과목의 순서가 주어집니다. 모든 과목은 영문 대문자입니다.
# 두 번째 줄에 N(1<=N<=10)이 주어집니다.
# 세 번 째 줄부터 현수가 짠 N개의 수업설계가 주어집니다.(수업설계의 길이는 30이하이다)
# 수업설계는 같은 과목을 여러 번 이수하도록 설계해도 됩니다.
# ▣ 출력설명
# 수업설계가 잘된 것이면 “YES", 잘못된 것이면 ”NO“를 출력합니다.
# ▣ 입력예제 1
# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA
# ▣ 출력예제 1
# #1 YES
# #2 NO
# #3 YES
# ▣ 입력예제 2
# AFC
# 1
# AFFDCCFF
# ▣ 출력예제 2
# #1 YES

# AKDEF
# 1
# WOPASFKGHDEF
# NO
# 이게 왜 NO 나면 WOPAS"F" 이 F 때문임
from collections import deque

def classDisgn(m, arr):
    res = "NO"
    m = deque(m)

    for i in arr:
        if m[0] == i:
            m.popleft()
        elif i in m:
            break

    if not m:
        res = "YES"

    return res

def inputFnc():
    mArr = list(map(str,input()))
    t = int(input())
    classArr = []
    for _ in range(t):
        tmp = list(map(str,input()))
        classArr.append(tmp)

    return mArr, t, classArr

mustClass, T, classArr = inputFnc()

for i in range(T):
    res =classDisgn(mustClass, classArr[i])
    print("#%d %s" %(i+1,res))


