#  0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())

        dp = [i for i in range(1,n+1)]

        for _ in range(k):
            for i in range(n-1,0,-1):
                for j in range(i):
                    dp[i] += dp[j]

        print(dp[n-1])



# 1 2 3
# 1 3 6
# 1 4 10