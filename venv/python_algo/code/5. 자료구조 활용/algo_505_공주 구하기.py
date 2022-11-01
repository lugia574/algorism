# N 명이 있는데 서로 공주 구한데
# 둘러 앉아  K 인 사람은 계속 뺀데
# 그래서 한명 남을때 까지 ㄱㄱ
#
# ▣ 입력설명
# 첫 줄에 자연수 N(5<=N<=1,000)과 K(2<=K<=9)가 주어진다.
# ▣ 출력설명
# 첫 줄에 마지막 남은 왕자의 번호를 출력합니다.
# ▣ 입력예제 1
# 8 3
# ▣ 출력예제 1
# 7

def savingPrincess(n, k):
    arr = [i for i in range(1,n+1)]
    cnt = 0
    index = 0
    while len(arr) > 1:
        cnt += 1
        if cnt == k:
            del arr[index]
            cnt = 0
            index -= 1
        index += 1
        if len(arr) == index:
            index = 0
    return arr[0]

def inputFnc():
    n, m = map(int,input().split())
    return  n, m

N, K = inputFnc()
res = savingPrincess(N,K)
print(res)