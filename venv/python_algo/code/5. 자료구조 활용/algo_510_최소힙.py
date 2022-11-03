# 최소힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램을 작성하세요.
# 1) 자연수가 입력되면 최소힙에 입력한다.
# 2) 숫자 0 이 입력되면 최소힙에서 최솟값을 꺼내어 출력한다.
#  (출력할 자료가 없으면 -1를 출력한다.)
# 3) -1이 입력되면 프로그램 종료한다.
# ▣ 입력설명
# 첫 번째 줄부터 숫자가 입력된다. 입력되는 숫자는 100,000개 이하이며 각 숫자의 크기는 정수형 범위에 있다.
# ▣ 출력설명
# 2) 연산을 한 결과를 보여준다.
# ▣ 입력예제 1
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
# ▣ 출력예제 1
# 3
# 5
# 2

# 힙을 쓰는 이유
# https://frootjy.tistory.com/22

import heapq as hq

def minHeap():
    arr = []
    while True:
        num = int(input())
        if num == -1:
            break
        if num == 0:
            if len(arr) == 0:
                print(-1)
            else:
                print(hq.heappop(arr))
        else:
            hq.heappush(arr,num)


arr = minHeap()