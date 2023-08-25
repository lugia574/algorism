# 모야모야 이거 dp 자너? 아닌가 정렬문제인거 같기도 한데
# 하루에 한번 과제씩 해결하는거고 하니까 정렬 그리드 문제가 맞기도 하고 아닌가 dp 로 할 수  있나?
# 3 30 > 2 50 > 4 40 > 4 60 > 6 5
# 아 어렵다 젠장
# https://velog.io/@heyksw/Python-백준-gold-13904-과제
# 이게 어제인가 엊그제인가 풀었던 옥상정원 꾸미기랑 비슷한 맥락이긴한데
# 아 이게 문제를 보면 어떻게 풀것인지 바로바로 구상이 안돼 ㅅㅂ
# 자 설명 드갈께
# 핵심은 점수야
# 근데 마감일에 최대한 가깝게 해서 과제를 해야지
# 가령 6일까지 기한이고 점수가 젤 높아  그리고 담으로 높은 게 기한은 1일이야
# 이때 단순히 점수 높은것들 위주로 쳐내면 6일치꺼 먼저 하다가 두번째로 높은 얘를 놓치게 되는거자너
# 그러니까 높은애들 위주로 하되 최대한 미루어서 날을 잡게 구현을 해야지

# 그러기 위해선 우선 점수 내림차순으로 정렬을 해
# 그리고 그 높은 순으로 정렬된 점수 기한일에 그 과제를 한다고 해
# 근데 만약에 그 날이 이미 차있다? (하루에 하나씩 밖에 못함 총 N 일까지 과제 가능)
# 그럼 -1 씩 하면서 그 전날은 비어 있는지 확인하고 비어잇으면 그 날에 하면 되는거지
# 가령 기한 4일 얘를 받았다고 쳐 그럼 4일날에 비어있는지 확인하고 차있으면 3일 2일 이렇게 내려가는거야
# 그리고 그 값을 ++ 해주는거지 끝끝
# 원리자체는 쉬운데 이걸 구상할 머리빡이 안되는 나에게 치얼스!
import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    time = [False] * 1001
    arr.sort(key= lambda x: x[1], reverse=True)
    answer = 0

    for day, score in arr:
        i = day
        while i > 0 and time[i]:
            i -= 1
        if i == 0: continue
        else:
            time[i] = True
            answer += score

    print(answer)


