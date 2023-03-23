import sys

# 아직 잘 이해안감
# 뭔소리 하는지 알아먹는데
# 솔직히 몇일 지나고 그냥 문제만 쥐어주고 풀어보라 하면 100프로 못풀듯

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    sq = list(map(int, input().split())) # 값 받기
    dp = [1] * n # dp 선언 및 초기화

    for i in range(n):
        for j in range(i): # sq Arr 가 처음부터 i - 1 번째까지 돌아
            if sq[i] > sq[j]: # 현재 i 위치의 arr 값이 j 위치 arr 값보다 클때
                dp[i] = max(dp[i], dp[j] + 1) # 현재 dp 값과 dp[j] + 1 값을 비교해서 더 큰값으로 갱신 해줌
        #print(dp)

    print(max(dp))




# 6
# 90 20 90 30 20 50
# 3

# 6
# 10 20 10 30 20 50

