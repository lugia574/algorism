# 조합 구하기
# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑는 방법의 수를 출력하는 프로그
# 램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
# ▣ 출력설명
# 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
# 출력순서는 사전순으로 오름차순으로 출력합니다.
# ▣ 입력예제 1
# 4 2
# ▣ 출력예제 1
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# 6
import copy


def combination(index):
    global cnt
    if index == m:
        if mArr:
            for i in mArr:
                mCnt = 0
                for j in check:
                    if j in i:
                        mCnt += 1
                if mCnt == m:
                    return
        for i in check:
            print(i, end=" ")
        print()
        cnt += 1
        tmp = copy.copy(check)
        mArr.append(tmp)
    else:
        for i in range(1, n+1):
            if i not in check:
                check[index] = i
                combination(index+1)
                check[index] = 0

if __name__ == "__main__":
    n,m = map(int,input().split())
    check = [0] * m
    mArr = []
    cnt = 0

    combination(0)
    print(cnt)