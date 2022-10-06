# 사과나무
# N*N 격자판(N 은 항상 홀수임)
# 그중 다이아몬드 모양의 격자판만 수확
# 수확하는 사과의 총 개수를 출력
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

def arrSum(N,arr):
    res = 0
    start = N//2 # 2
    end = N//2 + 1 # 3

    for i in range(N):
        if i < N//2:
            #print("i의 값: ",i,"증가",arr[i][start:end])
            res += sum(arr[i][start:end])
            start -= 1
            end += 1
        elif i == N//2:
            #print("i의 값: ", i, "동일", arr[i][start:end])
            res += sum(arr[i][start:end])
        else:
            start += 1
            end -= 1
            #print("i의 값: ",i,"감소",arr[i][start:end])
            res += sum(arr[i][start:end])
    return res


N = int(input())

arr = [0 for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

res = arrSum(N,arr)

print(res)