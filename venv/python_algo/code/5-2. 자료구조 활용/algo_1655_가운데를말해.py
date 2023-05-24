# 하 시바 도시바 그냥 힙써서 정렬된 배열에 중간 idx 하면 되는거 아녀? 했는데 안됨 ㅋ
# 애초에 값조차 제대로 못부름 정렬이 내가 생각한데로 안됨 ㅋ
# 하긴 그냥 sort 처럼 됐음 sort 를 안썻지 ㅋㅋ
# ======
# 아무튼 이 문제를 풀려면 두개의 힙이 필요함
# left 힙 - 가운데값 - right 힙 이런식으로 할꺼란 말이야
# 이런식으로 할려면 left 가 최대힙이여야해 그래서 값을 넣을때 -num 해서 넣어줄꺼야

# 내가 만약에 했다면 양 힙에 비어있는지 확인해서 비었음 거기에 넣어주고
# 둘다 채워져 있으면 양 힙 값을 비교해서 어디에 넣냐 어쩌냐 했을꺼 같은데
# 그럼 너무 길어지고 난해해

# 우선적으로 len 값이 같으면 left에 박아 넣어 (0==0 이면 무조건 left 이후에 1==0 되면 right)
# 박아넣어지면서 정렬된 양 힙의 맨위값을 비교해서 옮겨주는거야
# 그리고 나서 left 맨 위 값을 출력하는거지

import sys, heapq as hq

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    left = []
    right = []
    for i in range(n):
        num = int(input())
        if len(left) == len(right):
            hq.heappush(left, -num)
        else:
            hq.heappush(right, num)

        if right and right[0] < -1 * left[0]:
            leftValue = hq.heappop(left) * -1
            rightValue = hq.heappop(right) * -1
            hq.heappush(left, rightValue)
            hq.heappush(right, leftValue)
        print(left[0] * -1)
