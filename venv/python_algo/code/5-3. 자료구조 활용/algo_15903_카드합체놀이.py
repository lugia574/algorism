import sys, heapq

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    q = []
    for x in list(map(int, input().split())):
        heapq.heappush(q, x)

    for _ in range(m):
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        z = x + y
        heapq.heappush(q, z)
        heapq.heappush(q, z)

    print(sum(q))
