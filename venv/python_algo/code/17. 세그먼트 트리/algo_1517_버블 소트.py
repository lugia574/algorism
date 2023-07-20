# 이러면 무조건 터짐
# https://www.youtube.com/watch?v=ctkuGoJPmAE&t=328s
# 이렇게 merge sorted 방법으로 푸는 방법이 있고
# https://peisea0830.tistory.com/51
# 이렇게 펜윅트리 방법으로 푸는 방법이 있는데
# 근데 사실 펜윅트리나 머지소트나 똑같애
# 어차피 반반 나눠서 재귀로 들어가는거자너
# 그럼 어차피 NlogN 정도로 먹고 들어가는거고
import sys

def mergeSort(start, end):
    global swapCnt, arr
    if start >= end: return
    mid = start + (end - start) // 2
    mergeSort(start, mid)
    mergeSort(mid+1, end)

    x, y = start, mid+1
    sortArr = []

    while x <= mid and y <= end:
        if arr[x] <= arr[y]:
            sortArr.append(arr[x])
            x += 1
        else:
            sortArr.append(arr[y])
            y += 1
            # arr[x]보다 큰 값들은 arr[y]부터 arr[mid]까지의 범위에 존재하므로, Swap이 발생한 횟수는 (mid - x + 1)
            swapCnt += (mid - x + 1)

    if x <= mid:
        sortArr = sortArr + arr[x:mid+1]
    if y <= end:
        sortArr = sortArr + arr[y:end+1]

    for i in range(len(sortArr)):
        arr[start+i] = sortArr[i]




if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    swapCnt = 0
    mergeSort(0, n-1)
    print(swapCnt)