import sys, heapq as hq

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    cards = [int(input()) for _ in range(n)]
    hq.heapify(cards)
    cost = 0

    while len(cards) > 1:
        tmp = hq.heappop(cards) + hq.heappop(cards)
        hq.heappush(cards, tmp)
        cost += tmp
    print(cost)

