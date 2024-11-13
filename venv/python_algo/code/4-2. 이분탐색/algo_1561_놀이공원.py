# 이건 뭔소리냐 우선
# N(1 ≤ N ≤ 2,000,000,000), M(1 ≤ M ≤ 10,000) 이래서 무조건 시복 log 급으로 조져야함
# 그럼 이분탐색인데 대체 뭘 기준으로 하는거야
# 그냥 각 놀이기구가 수용할 수 있는 인원수로 cnt 해서 업다운 갈기고
# lt 반환 하면 어떻게든 되지 않을까? ㅋㅋㅋ 아 걍 우겨 집어넣어봐 ㅋㅋ 는 역시 안됨 ㅋ
# 애초에 뭘 하겠다는건지 ㅋㅋ
# https://hbj0209.tistory.com/175
# 아따 이 문제는 좀 꼬아진 문제다
# 한번에 답에 도달 할 수가 없어 한번 역산을 해줘야해
# 이게 골드2 라고? ㅋ 말이 안됨 ㅋ
# 암튼 차근차근 해보자
# 1. N 명이 총 타게 되는 시간을 구하자
# 2.
# 하 시바 난 좀 이해가 안가
# 을마나 탓나를 먼저 cnt 하는것부터가 이해가 안가
# 왜 cnt = 0 으로 시작 안하고 cnt = m 부터 시작하는거지?
# 왜 미리 다 타고 있는 상황을 상정해서 시작하는거지?
# 대충 보면 cnt = 0 로 시작해서 돌리면 cnt >= n 이라는 조건이 만족하지 못해
# 그래서 결국 제대로 못돌아 버리긴하는데
# 그게 맞냐 이거야 왜 못도냐 이거야
# 하 우선 쉬운거 위주로 풀자 ㅅㅂ

import sys



if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    times = list(map(int, input().split()))

    start, end = 0, 2_000_000_000_000_000_000  # N의 최댓값 x M의 최댓값
    total_time = 0  # n명까지 놀이기구를 모두 타는데 걸리는 시간

    while start <= end:  # total_time을 이진탐색으로 구해준다.
        mid = (start + end) // 2
        is_possibe = False
        cnt = m
        for time in times:
            cnt += mid // time
            if cnt >= n:
                is_possible = True
        if is_possible:  # 현재 mid값(tmp_total_time) 안에 n보다 많은 사람이 탈수 있으면
            total_time = mid
            end = mid - 1
        else:  # 현재 mid 값 안에 n이 충분히 탈 수 없으면
            start = mid + 1

    tmp_person = m  # 현재 놀이기구를 탄사람의 수, 0초에 m명이 탈수있으므로 m값으로 초기화
    for time in times:
        tmp_person += (total_time - 1) // time  # total_time의 1초 전 몇명까지 탈 수 있는지?

    for index, time in enumerate(times, 1):
        if total_time % time == 0:  # total_time일 때, 기구가 비어있으면 현재사람 += 1
            tmp_person += 1
        if tmp_person == n:  # 현재사람(tmp_person)이 마지막 n번째이면 print
            print(index)
            break