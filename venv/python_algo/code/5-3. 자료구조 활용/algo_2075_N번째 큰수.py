import sys, heapq
if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    hq = []

    for _ in range(n):
        for x in list(map(int,input().split())):
            if len(hq) == 0:
                heapq.heappush(hq, x)
                continue
            if hq[0] < x:
                heapq.heappush(hq, x)
            if len(hq) > n:
                heapq.heappop(hq)


    print(heapq.heappop(hq))