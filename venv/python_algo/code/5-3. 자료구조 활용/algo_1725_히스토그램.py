import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    stack = []
    maxSize = 0
    for i in range(n):
        idx = i
        while stack and stack[-1][0] >= arr[i]:
            num, idx = stack.pop()
            numSize = num * (i - idx)
            maxSize = max(maxSize, numSize)
        stack.append([arr[i], idx])

    for h, i in stack:
        maxSize = max(maxSize, h * (n-i))

    print(maxSize)