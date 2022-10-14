# 봉우리
# 지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 각 격자
# 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개
# 있는 지 알아내는 프로그램을 작성하세요.
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
# 만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.
# ▣ 입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
# 다.
# ▣ 출력설명
# 봉우리의 개수를 출력하세요.
# ▣ 입력예제 1
# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2
# ▣ 출력예제 1
# 10
def listAppend(n, arr):
    for i in range(n):
        arr[i].append(0)
        arr[i].insert(0, 0)

    tmpArr = [0]*(n+2)
    arr.insert(0, tmpArr)
    arr.append(tmpArr)

    return  arr

def peaksCounter(n,peaksList):
    cnt = 0
    peaksList = listAppend(n,peaksList)

    for i in range(1 , n+1):
        for j in range(1, n+1):
            if peaksList[i][j] > peaksList[i-1][j] and peaksList[i][j] > peaksList[i][j-1] and peaksList[i][j] > peaksList[i+1][j] and peaksList[i][j] > peaksList[i][j+1]:
                cnt +=1

    return cnt

N = int(input())

peaksList = [list(map(int,input().split())) for _ in range(N)]

# for x in peaksList:
#     print(x)

ans = peaksCounter(N,peaksList)

print(ans)