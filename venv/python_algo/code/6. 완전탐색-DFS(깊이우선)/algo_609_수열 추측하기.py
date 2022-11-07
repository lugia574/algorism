# N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램을 작성하
# 시오. 단, 답이 여러가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력하여야 한다.
# ▣ 입력설명
# 첫째 줄에 두개의 정수 N(1≤N≤10)과 F가 주어진다. N은 가장 윗줄에 있는 숫자의 개수를 의
# 미하며 F는 가장 밑에 줄에 있는 수로 1,000,000 이하이다.
# ▣ 출력설명
# 첫째 줄에 삼각형에서 가장 위에 들어갈 N개의 숫자를 빈 칸을 사이에 두고 출력한다. 답이 존재
# 하지 않는 경우는 입력으로 주어지지 않는다.
# ▣ 입력예제 1
# 4 16
# ▣ 출력예제 1
# 3 1 2 4
import sys


def inputFnc():
    n, res = map(int, input().split())
    return  n, res

def pGuess (index):
    if index == n:
        arrSum = 0
        for i in range(n):
            arrSum += nArr[i] * w[i]

        if arrSum == res:
            for i in nArr:
                print(i, end=" ")
            sys.exit(0)
    else:   
        for i in range(1,n+1):
            if i not in nArr:
                nArr[index] = i
                pGuess(index+1)
                nArr[index] = 0


if __name__ == "__main__":
    n, res = inputFnc()
    nArr = [0] * n
    w = [1] * n
    for i in range(1, n):
        w[i] = round(w[i-1] * (n-i) / i)
    pGuess(0)

