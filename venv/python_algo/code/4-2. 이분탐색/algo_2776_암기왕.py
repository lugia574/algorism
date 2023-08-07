import sys

def binary(start, end, arr, num):
    answer = 0
    while start <= end:
        mid = start + (end - start)// 2
        if arr[mid] == num:
            answer = 1
            break
        if arr[mid] > num:
            end = mid-1
        else:
            start = mid + 1
    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        arrA = list(map(int, input().split()))
        arrA.sort()

        m = int(input())
        arrB = list(map(int, input().split()))
        for num in arrB:
            print(binary(0, n-1, arrA, num))
