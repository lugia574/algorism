# 회의실 배정(그리디)
# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들
# 려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하
# 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 단, 회의는 한번 시작하면 중간에 중
# 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# ▣ 입력설명
# 첫째 줄에 회의의 수 n(1<=n<=100,000)이 주어진다. 둘째 줄부터 n+1 줄까지 각 회의의 정
# 보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# ▣ 출력설명
# 첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라.
# ▣ 입력예제 1
# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7
# ▣ 출력예제 1
# 3
# 예제설명
# (2, 3) , (3, 5), (5, 7)이 회의실을 이용할 수 있다.

# 그리드 알고리즘을 해
# 정렬을 하고 걍 돌리면 된다는데

def meetingFnc (n, arr):
    res = 1
    length = round(n**(1/2))//2
    for i in range(length):
        cnt = 1
        end = arr[i][1]
        for j in range(i+1,n):
            if end <= arr[j][0]:
                cnt += 1
                end = arr[j][1]
        if cnt > res:
            res = cnt


    return  res


# 시발 지리네 난 2중 포문 밖에 생각 안했는데 개 시발 나는 아직도 한참 멀었다 머리통을 존나 때려야해
def solution (arr):
    cnt = 0
    endTime = 0

    for s, e in arr:
        if s >= endTime:
            endTime = e
            cnt += 1

    return cnt

N = int(input())

meetingList = []

for _ in range(N):
    meetingList.append(list(map(int,input().split())))

meetingList.sort(key=lambda x: (x[1],x[0]))
print(meetingList)

res = solution(meetingList)
print(res)