# 이걸 어떻게 풀어야하나
# 단순이 2등분 하는거면 모르겠는데
# M 등분을 해야하니까 감이 안서네
# 내 생각인데 결국 최대한 비슷하게 M 등분을 해야하는거자나?
# 딱 맞아 떨어지는 M등분의 임의 값을 내주고
# start, end 값으로 이분탐색을 n-1 해서 M등분한 임의값에 맞추게 하는거야
# 1 2 3 4 5 6 7 8 9 를 3등분 한다고 했을때 총합55 이고 3등분값은 대충 18이지
# 1 ~ 5 까지가 딱 15임 18보단 작음
# 그럼 흐으음 여기서 하나 올라가면 바로 15+6 으로 21 되버리는데 그럼 너무 크자너 흐으음
# 안넘게 커트 치면 지금이야 딱 15 근처로 된다지만 18보다 작은 애들이라 마지막 얘가 너무 비대해지는거 아닌가
# 흐으음 아무리 생각해도 이건 에반거 같은데
# 그냥 딱봐도 n 번째에 다 몰아 넣지 말고
# 한 두개 정도는 18보다 높아야할 경우가 있을꺼 아녀

# 내가 한짓이 뭐가 문제냐면
# m 등분할 최소 영상길이를 무조건 M등분한 값으로 고정해버리고
# 그걸 기준으로 이분탐색으로 얼마나 가져갈것인지를 정할려고 한거임
# M등 값을 이분탐색으로 정해야지 ㅋㅋ
# 처음 값으로 M 등분을 설정하고 시작할순 있는데 ㅋ 아예 고정해버리는게 말이 안됨 ㅋ

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    start = max(arr)
    end = sum(arr)

    while start <= end:
        mid = start + (end - start) // 2
        cnt = 0
        sumValue = 0
        for i in range(n):
            if sumValue + arr[i] > mid:
                cnt += 1
                sumValue = 0

            sumValue += arr[i]
        cnt += 1 if sumValue else 0

        if cnt <= m:
            end = mid - 1
        else:
            start = mid + 1

    print(start)

