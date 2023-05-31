import sys
def coinCounter(n, coins, k):
    coinCnt = 0
    for i in range(n-1, -1, -1):
        coinCnt += k // coins[i]
        k = k % coins[i]

    return coinCnt

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().rsplit())
    coins = [int(input()) for _ in range(n)]
    answer = coinCounter(n, coins, k)
    print(answer)