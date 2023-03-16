# nCr 이 어떻게 되는지 함 만들어보자
# 단순 재귀적으로 만들면 쌉 ㅄ이니까 dp 을 이용해서 구현해보자


# https://www.youtube.com/watch?v=Uzgz4c7SzBw

def comb(n, r):
    if dp[n][r] != 0:
        return dp[n][r]
    if r == 0 or n == r:
        dp[n][r] = 1
        return dp[n][r]
    else:
        dp[n][r] = comb(n-1, r-1) + comb(n-1, r)
        return dp[n][r]

if __name__ == "__main__":
    n = 5
    r = 2

    dp = [[0] * (r+1) for _ in range(n+1)]

    res = comb(n,r)
    print(res)
    print(dp)


    # 방안2
    dp = [[0] * (r + 1) for _ in range(n + 1)]

    for i in range(n+1):
        for j in range(min(i, r) + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print(dp[n][r])
    print(dp)

    # 여기서 만약에 이항계수라고 했을때
    # (n,k) = (n / n-k) :k 가 n/2 보다 클 경우 == nCn-r
    # 좀 더 효율 적으로 할 수 있음
    
    # 또한 그냥 2차원 dp 가 아니라 1차원 dp 로도 구현 쌉가능임

    def bin3(n, k):
        if n // 2 < k:
            k = n - k
        check = [0] * (k+1)
        check[0] = 1

        for i in range(1, n+1):
            j = min(i, k)
            while(j>0):
                check[j] = check[j] + check[j-1]
                j -= 1

        return check[k]