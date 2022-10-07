# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
# 니다.
# ▣ 입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
# 다.
# ▣ 출력설명
# 최대합을 출력합니다.
# ▣ 입력예제 1
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# ▣ 출력예제 1
# 155


def arrMaxSum(N, arr):
    arr = np.array(arr)
    res = -2147000000
    for i in range(N):
        if sum(arr[i][:]) > res:
            print("가로: ",arr[i][:],sum(arr[i][:]))
            res = sum(arr[i][:])


            print("세로: ", arr[0:N][i], sum(arr[0:N][i]))
            if sum(arr[0:N][i])> res:
                res = sum(arr[:][i])
    x1 = 0
    x2 = 0
    for i in range(N):
        x1 += arr[i][i]
        x2 += arr[i][N-i-1]

    if x1 > res:
        res = x1
    if x2 > res:
        res = x2

    return res

def arrLargest(N, arr):
    largest = -2147000000
    for i in range(N):
        sum1 = sum2 = 0
        for j in range(N):
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        if sum1 > largest:
            largest = sum1
        if sum2 > largest:
            largest = sum2

    x1 = x2 = 0
    for i in range(N):
        x1 += arr[i][i]
        x2 += arr[i][N - i - 1]

    if x1 > largest:
        largest = x1
    if x2 > largest:
        largest = x2

    return largest

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

# arr = [0 for _ in range(N)]
#
# for i in range(N):
#     arr[i] = list(map(int, input().split()))

res = arrLargest(N,arr)

print(res)