# 수들의 조합
# N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수
# 는 몇 개가 있는지 출력하는 프로그램을 작성하세요.
# 예를 들면 5개의 숫자 2 4 5 8 12가 주어지고, 3개를 뽑은 조합의 합이 6의 배수인 조합을
# 찾으면 4+8+12 2+4+12로 2가지가 있습니다.
# ▣ 입력설명
# 첫줄에 정수의 개수 N(3<=N<=20)과 임의의 정수 K(2<=K<=N)가 주어지고,
# 두 번째 줄에는 N개의 정수가 주어진다.
# 세 번째 줄에 M이 주어집니다.
# ▣ 출력설명
# 총 가지수를 출력합니다.
# ▣ 입력예제 1
# 5 3
# 2 4 5 8 12
# 6
# ▣ 출력예제 1
# 2
import copy


def numsCombination(index, numsSum):
    global cnt
    if index == k:
        if numsSum % m == 0:
            if mcheck:
                for x in mcheck:
                    mCnt = 0
                    for i in check:
                        if i in x:
                            mCnt += 1
                    if mCnt == k:
                        return
            tmp = copy.copy(check)
            mcheck.append(tmp)
            cnt += 1

    else:
        for i in nArr:
            if i not in check:
                check.append(i)
                numsCombination(index+1, numsSum + i)
                check.pop()
def inputFnc():
    n, k = map(int,input().split())
    nArr = list(map(int,input().split()))
    m = int(input())
    return n,k,nArr,m

if __name__ =="__main__":
    n, k, nArr, m = inputFnc()
    check = []
    mcheck = []
    cnt = 0

    numsCombination(0, 0)
    print(cnt)
