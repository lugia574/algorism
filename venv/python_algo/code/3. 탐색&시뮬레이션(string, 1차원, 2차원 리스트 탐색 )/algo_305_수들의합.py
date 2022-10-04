# 수들의 합
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의
# 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
# ▣ 입력설명
# 첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …,
# A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
# ▣ 출력설명
# 첫째 줄에 경우의 수를 출력한다.
# ▣ 입력예제 1
# 8 3
# 1 2 1 3 1 1 1 2
# ▣ 출력예제 1
# 5

def numSum(N,M, numList):
    res = 0
    for i in range(N):
        if numList[i] == M:
            res += 1
            continue

        plus = []
        for j in range(i+1,N):
            if numList[j] + sum(plus) == M:
                res += 1
                break

            elif numList[j] + sum(plus) > M:
                break

            else:
                plus.append(numList[j])
    return res

def numSum2(N,M, numList):
    cnt = 0
    start = 0
    end = 1
    total = numList[0]

    while True:
       if total < M :
           if end < N:
               total += numList[end]
               end += 1
           else:
               break
       elif total == M:
           cnt += 1
           total -= numList[start]
           start += 1
       else:
           total -= numList[start]
           start += 1

    return cnt

N, M = map(int,input().split())

numList = list(map(int, input().split()))
print(numSum2(N,M,numList))