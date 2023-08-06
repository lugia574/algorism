import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    q = deque(i for i in range(1, n+1))
    answer = []

    for _ in range(n):
        num = q.popleft()
        answer.append(num)
        move = arr[num-1]
        if len(q) == 0: break
        if move > 0:
            for _ in range(move-1):
                q.append(q.popleft())

        else:
            for _ in range(abs(move)):
                q.appendleft(q.pop())

    print(*answer)
