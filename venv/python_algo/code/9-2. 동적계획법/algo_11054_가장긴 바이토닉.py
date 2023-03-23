import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))

    increase, decrease = [1] * n, [1] * n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                increase[i] = max(increase[i], increase[j]+1)

    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j]:
                decrease[i] = max(decrease[i], decrease[j]+1)

    print(increase)
    print(decrease)

    res = [0] * n
    for i in range(n):
        res[i] = increase[i] + decrease[i] -1

    print(res)

    print(max(res))