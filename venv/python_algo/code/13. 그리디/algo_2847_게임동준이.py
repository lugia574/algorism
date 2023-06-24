import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    cnt = 0
    num = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] >= num:
            cnt += arr[i] - num + 1
            arr[i] = num - 1
        num = arr[i]

    print(cnt)