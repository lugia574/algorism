# 송아지 찾기(BFS : 상태트리탐색)
# 위치가 직선상의 좌표 점으로 주어지면 송아지의 위치까지 다음과 같은 방법으로 이동한다.
# 현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다.
# 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성
# 하세요.
# ▣ 입력설명
# 첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000
# 까지이다.
# ▣ 출력설명
# 점프의 최소횟수를 구한다.
# ▣ 입력예제 1
# 5 14
# ▣ 출력예제 1
# 3
import sys
from collections import deque

if __name__ == "__main__":
    s, e = map(int,input().split())
    max = 10000
    cnt = 0
    check = [0] * (max + 1)
    dis = [0] * (max + 1)
    check[s] = 1
    dQ = deque()
    dQ.append(s)

    while dQ:
        now = dQ.popleft()
        if now == e:
            break
        for next in (now+1, now-1, now+5):
            if 0 <next <= max:
                if check[next] == 0:
                    dQ.append(next)
                    check[next] = 1
                    dis[next] = dis[now] + 1

print(dis[e])