import sys

input = sys.stdin.readline
n = int(input())
numArr = list(map(int, input().split()))


for i in range(1, n):
    numArr[i] = max(numArr[i], numArr[i] + numArr[i-1])

print(max(numArr))
