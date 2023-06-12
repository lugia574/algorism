# 역시 사람은 머리가 좋아야해
# hq 로 이렇게 쉽게 풀다니
# 나였음 이중 포문으로 어떻게 조물딱 조물딱 만져볼까 이런 생각 했을텐데
# 딱 힙으로 최소 값만 띄어서 이값보다 낮으면
# 하나 더 넣어주고
# 최소값보다 높으로면 최소값 pop 해주고 그값을 딱 넣어주고 캬 멋지다 멋져
import sys, heapq as hq

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    classTime = [list(map(int, input().split())) for _ in range(n)]
    classTime.sort()

    classRoom = []
    hq.heappush(classRoom, classTime[0][1])
    for i in range(1, n):
        if classTime[i][0] < classRoom[0]:
            hq.heappush(classRoom, classTime[i][1])
        else:
            hq.heappop(classRoom)
            hq.heappush(classRoom, classTime[i][1])

    print(len(classRoom))

