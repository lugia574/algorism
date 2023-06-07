# 끄아악 이러면 무조건 터진다!
# 와 최대힙 최소힙을 여기서 쓰네
# https://bio-info.tistory.com/195

# 아 내가 이해가 안갔었음
# tmp 에 최대힙으로 박으면서 왜 보석 배열을 빼버리야 이거야
# 다음 백에 넣을때 누락 되는거 아니냐~
# 근데 여기서 내가 tmp 를 아예 생각을 못했어
# 하나 뺀다고 tmp 에 아직 남아 있는 애들이 사라진줄 알았어
# 전혀 안사라지고 그대로 남아 있는데말이야 tmp 라고 써서 그런듯 ㄹㅇ ㅋㅋ

import sys, heapq as hq

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    gems = [[*map(int, input().split())] for _ in range(n)]
    bags = [int(input()) for _ in range(k)]
    gems.sort()
    bags.sort()
    tmp = [] # 최대힙
    res = 0
    for b in bags:
        while gems and b >= gems[0][0]:
            hq.heappush(tmp, -gems[0][1])
            hq.heappop(gems)

        if tmp:
            res -= hq.heappop(tmp)

    print(res)

# 4 2
# 1 65
# 5 23
# 2 99
# 2 101
# 10
# 2