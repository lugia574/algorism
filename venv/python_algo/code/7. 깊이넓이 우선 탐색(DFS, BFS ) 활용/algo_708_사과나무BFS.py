# ▣ 입력설명
# 첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
# 각 격자안의 사과의 개수는 100을 넘지 않는다.
# ▣ 출력설명
# 수확한 사과의 총 개수를 출력합니다.
# ▣ 입력예제 1
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# ▣ 출력예제 1
# 379
from collections import deque

def appleBFS():
    global level
    while True:
        if level == n//2+1:
            break
        else:
            size = len(d)
            for i in range(size):
                nowR, nowC = d.popleft()
                check[nowR][nowC] = 1
                for i in range(4):
                    if 0<= nowR+rc[i] < n and 0<= nowC+cc[i] < n:
                        if check[nowR+rc[i]][nowC+cc[i]] == 0:
                            d.append([nowR+rc[i],nowC+cc[i]])
            level+=1

if __name__== "__main__":
    n = int(input())
    appleArr = []
    d = deque()
    rc = [1, 0, -1, 0]
    cc = [0, 1, 0, -1]
    level = 0
    check = [[0] * n for _ in range(n)]
    for _ in range(n):
        tmp = list(map(int,input().split()))
        appleArr.append(tmp)

    start = [n//2,n//2]
    d.append(start)
    appleBFS()
    res = 0
    for i in range(n):
        for j in range(n) :
            if check[i][j] == 1:
                res += appleArr[i][j]
    print(res)
