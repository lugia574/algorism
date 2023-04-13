import heapq as hq
import sys


def absHeap(x):
    if x == 0:
        try:
            print(hq.heappop(h)[1])
        except:
            print(0)
    else:
        hq.heappush(h, [abs(x), x])


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    h = []
    for _ in range(n):
        x = int(input())
        absHeap(x)
