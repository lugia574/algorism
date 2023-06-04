# 내 풀이랑 비슷하네
# https://velog.io/@joniekwon/Python-백준-16953번-A-B
import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    st, ed = map(int, input().split())
    q = deque()
    q.append((st, 1))
    res = -1
    while q:
        num, cnt = q.popleft()
        if num == ed:
            res = cnt
            break
        if num < ed:
            for i in (num*2, ((num*10) + 1)):
                q.append((i, cnt+1))
    print(res)