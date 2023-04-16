# 냅색 알고리즘이란다
# 냅색 알고리즘에 dp 를 섞어서 푸는거래
# 냅색 알고리즘 https://velog.io/@uoayop/%EB%83%85%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# 냅색 알고리즘2 https://www.youtube.com/watch?v=rhda6lR5kyQ

# 자 어떻게 풀었는지 줄줄 읊어야지 이 문제를 넘어갈 수 있겠다
# 남에꺼 배껴서 낸 코드라 이해를 무조건 해야한다


import math
import sys

def knapsack(cost, app, n, m):
# 우선 만약에 n 이 1 이라면 코드 진행 할 것이 없으니 바로 cost[0] 를 반환
# m 이 1<= 이니까 0 일리는 없고 부족할 시 -1 을 출력하라는 조건도 없음 그냥 cost[0] 리턴하라 하면 됨
    if n == 1:
        return cost[0]

    length = sum(cost) # length 는 총 코스트값을 길이로 >> 이유는 최악의 경우 모든 앱을 비활성화 해야 할 수 도 있음
    dp = [[0] * (length + 1) for _ in range(n + 1)] # 그렇기에 열으로는 length 값으로 하고 행은 각 앱들의 갯수 만큼 dp 를 생성
    res = math.inf # 이것은 결과값 math.inf 최고값으로 해서 포문을 돌면서 계속 갱신 해줄꺼임

    # 자 이제 포문을 돌꺼에여 
    for i in range(n):
        for j in range(length+1):
            # j 는 sum(cost) 값까지 돌껀데 j 값과 cost[i] 값과 비교해서 cost 값이 더 크면 적합하지 않으니까
            if cost[i] > j:
                # 그냥 전에 값을 가져가다가 채움 이러면 cost[i] 이 작아지는 순간 부터는 cost[i] 값이 포함되게 값이 넣어지겠지
                dp[i][j] = dp[i-1][j]
            else:
                # 여기서 단순히 값을 넣는게 아니라 이전값 dp[i-1][j] 이 더 큰지 아니면 현재 app 값에 dp[i-1][j-cost[i]] 코스트 값을 뺀 j 값을 합친게 더 큰지 따져서 갱신
                dp[i][j] = max(dp[i-1][j], app[i] + dp[i-1][j-cost[i]])
            
            # 갱신한 값이 목표 무게 m 과 같거나 혹은 더 높으면
            # res 값을 비교 때려서 갱신해줘
            if dp[i][j] >= m:
                res = min(res, j)

    # 이러면 대충 n^2 시간 복잡도를 가지겠지 뭐
    # 만약에 갱신이 안되서 math.inf 값이 그대로라면?
    # 그러면 최대값인 n * m ? ??? 이러면 cost 총값을 뱉어야하는거 아닌가???
    # 아닌가 애초에 갱신이 안될리가 없고 그리고 cost 총값 까지 염두에 두고 짠건데  흠 왜 n * m 을 하는거지?
    # n * m 부분을 빼고 하니까 틀렸네 뭐지 length 값으로 대체 하니까 또 됐음 뭐냐 ㅋㅋㅋ
    return (res if res < math.inf else length)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    app = list(map(int,input().split()))
    cost = list(map(int,input().rsplit()))
    res = knapsack(cost, app, n, m)
    print(res)