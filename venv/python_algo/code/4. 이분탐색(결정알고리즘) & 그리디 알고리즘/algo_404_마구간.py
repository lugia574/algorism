# N개의 마구간 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
# 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을
# 마구간에 배치하고 싶습니다.
# C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대
# 값을 출력하는 프로그램을 작성하세요.
#
# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
# 둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩
# 주어집니다.
# ▣ 출력설명
# 첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.
# ▣ 입력예제 1
# 5 3
# 1
# 2
# 8
# 4
# 9
# ▣ 출력예제 1
# 3

# 1 2 4 8 9

def interLenCnt(capacity,arr):
    cnt = 1
    start = min(arr)
    for i in range(1,len(arr)):
        if  arr[i] - start >= capacity:
            cnt += 1
            start = arr[i]

    return cnt

def intervalMaxLength (h, arr):
    res = 0
    lt = 1
    rt = max(arr)

    while lt <= rt:
        mid = (lt + rt) // 2
        if interLenCnt(mid, arr) >= h:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    return res

N, horses = map(int,input().split())
room = []

for _ in range(N):
    room.append(int(input()))

room.sort()
res = intervalMaxLength(horses, room)

print(res)