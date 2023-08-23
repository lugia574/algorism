# 이거 처음에 볼땐 허씨 이거 뭔 ㅈㄹ 이여 생각했는데
# 그냥 힙큐 에 박아 넣어버리면 되자너~
# 제일 큰순위로 하고 맨 위 값 -1 하고 다시 넣고
# 근데 이래도 되나 ㅋ 1 씩 빼는거 너무 ㅎㅌㅊ 아님? ㅋㅋ 뭐 N은 50까지고 득표수가 100 차이 밖에 안난다니까 할만하것지
# 띠요옹 92퍼 인덱스 에러 뭐냐 
# ㅋ n == 1 일때 실화냐 ㅋ 그래도 금방 찾음 ㅋ
import sys, heapq

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    target = int(input())
    res = 0
    arr = []

    if n > 1:
        for _ in range(n-1):
            heapq.heappush(arr, int(input()) * -1)

        while True:
            x = heapq.heappop(arr) * -1
            if target > x:
                break
            else:
                x -= 1
                heapq.heappush(arr, x * -1)
                target += 1
                res += 1
    print(res)

