# 모든 B는 BA로 바뀌고, A는 B로 바뀐다
# 처음 시작은 A 이고 한번 누르면 B 딱 이것만 되니까 0 1
# 두번 누르면 A > B > BA 가 되겠지? 그럼 1 1
# 세번 누르면 A > B > BA > BA B  1 2
# 네번 누르면 A > B > BA > BA B > BA B BA > 2 3
# 다섯번                         BA B BA BA B > 3 5
import sys

def BABBA(n):
    dp = [0]
    dp.append((0, 1))

    for i in range(2, n+1):
        a, b = dp[i-1]
        dp.append((b, b+a))

    return dp[n]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    A,B = BABBA(n)
    print("%d %d"%(A, B))