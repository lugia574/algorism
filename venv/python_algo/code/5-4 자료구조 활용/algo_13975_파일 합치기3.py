# 그냥 되지 않을까 하고 짜서 냈는데 존나 힘겹게 하고 성공하긴함 ㅋㅋ
# 파일합치기 1 이거 보니까 뭔 3중 루프를 돌리는데 이럼 무조건 시초 걸릴듯 ㅋㅋ
import sys, heapq

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        k = int(input())
        arr = []
        cost = 0
        for i in list(map(int, input().split())):
            heapq.heappush(arr, i)

        while len(arr) > 1:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)
            cost += x + y
            heapq.heappush(arr, x + y)

        print(cost)
