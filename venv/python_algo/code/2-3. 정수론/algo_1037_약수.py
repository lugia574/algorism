import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(arr[0] ** 2)
    else:
        arr.sort()
        print(arr[0] * arr[n-1])