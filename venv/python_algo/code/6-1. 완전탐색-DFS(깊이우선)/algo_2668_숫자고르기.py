# https://moonsbeen.tistory.com/176
# 심각하다 심각해 지금

import sys
from collections import deque

def dfs(x, y, num):
    x.add(num)
    y.add(arr[num-1])
    if arr[num-1] in x:
        if x == y:
            answer.update(x)
            return True
        return False
    return dfs(x, y, arr[num-1])

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    answer = set()


    for i in range(1, n+1):
        if i not in answer:
            dfs(set(), set(), i)

    print(len(answer))
    print(*sorted(list(answer)), sep=" \n")


