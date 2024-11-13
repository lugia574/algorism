# 문제) N 개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있음
#       이때 수열에서 수 X 가 등장하는 횟수를 계산하시오
# 이 문제는 시간복잡도 logN 으로 풀지 않을 시 시간초과 판정 받음
# 이 문제는 값이 특정 범위에 속하는 갯수 구하기로
# 정렬된 순서에서 가장 왼쪽 index 랑 가장 오른쪽 index 를 구해서 rt - lt 하면 됨

from bisect import bisect_left, bisect_right

def solution(n, x, arr):
    rt = bisect_right(arr, x)
    lt = bisect_left(arr, x)
    answer = rt - lt
    return answer if answer > 0 else -1

def mySolution(n, x, arr):
    mid = n // 2
    rt = searchRight(mid, n-1, x, arr)
    lt = searchLeft(0, mid, x, arr)
    answer = rt - lt
    return answer if answer > 0 else - 1

def searchRight(start, end, x, arr):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == x:
            start = mid + 1
        else:
            end = mid - 1
    return start

def searchLeft(start, end, x, arr):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == x:
            end = mid - 1
        else:
            start = mid + 1
    return start

if __name__ == "__main__":
    n, x = 7, 2
    arr = [1, 1, 2, 2, 2, 2, 3]
    res = 4
    # ans = solution(n, x, arr)
    ans = mySolution(n, x, arr)
    print(res == ans, ans)
