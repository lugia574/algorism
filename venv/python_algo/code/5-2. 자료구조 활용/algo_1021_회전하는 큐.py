import sys
from collections import deque

def queFnc(arr, a):
    cnt = 0
    for x in a:
        length = len(arr)
        x_idx = arr.index(x)
        if x_idx < length - x_idx:
            while True:
                if arr[0] == x:
                    arr.popleft()
                    break
                tmp = arr.popleft()
                arr.append(tmp)
                cnt += 1
        else:
            while True:
                if arr[0] == x:
                    arr.popleft()
                    break
                tmp = arr.pop()
                arr.appendleft(tmp)
                cnt += 1
    return cnt

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    arr = deque()
    for i in range(1, n+1): arr.append(i)
    answer = queFnc(arr, a)
    print(answer)