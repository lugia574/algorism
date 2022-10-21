# 뭔소리야 시벌 암튼 N 개의 리스트 요소들을 섞지 않고 그대로
#  M 개로 구분한  DVD의 최소 용량 크기
# 그니까 M 그룹 중 젤 큰 값이 최소 용량인듯?
#
# ▣ 입력설명
# 첫째 줄에 자연수 N(1≤N≤1,000), M(1≤M≤N)이 주어진다. 다음 줄에는 조영필이 라이브에서
# 부른 순서대로 부른 곡의 길이가 분 단위로(자연수) 주어진다. 부른 곡의 길이는 10,000분을
# 넘지 않는다고 가정하자.
# ▣ 출력설명
# 첫 번째 줄부터 DVD의 최소 용량 크기를 출력하세요.
# ▣ 입력예제 1
# 9 9
# 1 2 3 4 5 6 7 8 9
# ▣ 출력예제 1
# 17
# 설명 : 3개의 DVD용량이 17분짜리이면 (1, 2, 3, 4, 5) (6, 7), (8, 9) 이렇게 3개의 DVD로 녹음을 할
# 수 있다. 17분 용량보다 작은 용량으로는 3개의 DVD에 모든 영상을 녹화할 수 없다.
# 1 2 3 / 4 5 6 / 7 8 9  >> 6 / 15 / 24
def dvdCuttingFnc (n,m,arr):
    res = 0
    start = 1
    end = sum(arr)

    while start <= end :
        mid = (start + end) // 2

        if mid >= max(arr) and counterFnc(mid, arr) <= m:
            end = mid - 1
            res = mid
        else:
            start = mid + 1

    return res

def counterFnc(capacity, arr):
    cnt = 1
    sum = 0
    for x in arr:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else :
            sum += x
    return cnt

def solution (n,m,arr):
    lt = 1
    rt = sum(arr)
    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        maxMusic = max(arr)
        if mid <= maxMusic and counterFnc(mid, arr) <= m:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1
    return  res

N,M = map(int, input().split())

musicList = list(map(int, input().split()))

dvdMinLength = dvdCuttingFnc(N,M,musicList)

print(dvdMinLength)



