# 최솟값 구하기
arr = [5,3,7,9,2,5,2,6]

min_nim = float('inf') # 파이썬에서 가장 큰값

for i in range(len(arr)):
    if arr[i] < min_nim:
        min_nim = arr[i]

