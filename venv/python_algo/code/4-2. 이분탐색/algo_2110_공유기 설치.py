# 하씨 이게 어떻게 구현하는지가 너무 머리가 안돌가
# 지금 보면 주어진 c 개의 공유기를 설치해서 최대 공유기 거리를 구하는거자나
# 그니까 거리의 최소값 1, 최대값 loc 의 최소값, 최대값 뺀값 부터 시작해
# 여기까진 ㅈ밥이야
# 여기서 이 mid 값이 많은지 적은지를 판별하는 알고리즘을 잘 못짜겠다 이거야 시벌
# 이 문제는 거리값이자나 그러니까
# loc 포문을 돌면서 cur(현재위치값) + mid 값을 넘으면 박고 cnt 해주는거야
# 그렇게 포문 쭉 돌아서 cnt 가 c 값을 넘냐 안넘냐로 lt, rt 값을 갱신을 해줌
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, c = map(int, input().rsplit())
    loc = [int(input()) for _ in range(n)]

    loc.sort()
    lt = 1
    rt = loc[-1] - loc[0]

    while lt <= rt:
        mid = (lt + rt) // 2
        curloc = loc[0]
        cnt = 1
        for i in range(1, n):
            if loc[i] > curloc + mid:
                cnt += 1
                curloc = loc[i]
        if cnt >= c:
            lt = mid + 1
        else:
            rt = mid - 1
    print(lt)