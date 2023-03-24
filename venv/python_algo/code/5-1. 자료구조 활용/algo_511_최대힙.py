import heapq as hq
# 5
# 3
# 6
# 0
# 5
# 0
# 2
# 4
# 0
# -1
def maxHeap():
    arr = []
    while True:
        num = int(input())
        if num == -1:
            break
        if num == 0:
            if len(arr) == 0:
                print(-1)
            else:
                print(-hq.heappop(arr))
        else:
            hq.heappush(arr,-num)


maxHeap()