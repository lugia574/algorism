import sys

# 아직 잘 이해안감
# 뭔소리 하는지 알아먹는데
# 솔직히 몇일 지나고 그냥 문제만 쥐어주고 풀어보라 하면 100프로 못풀듯

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    sq = list(map(int, input().split()))
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if sq[i] > sq[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        print(dp)

    print(max(dp))




# 6
# 90 20 90 30 20 50
# 3

# 6
# 10 20 10 30 20 50