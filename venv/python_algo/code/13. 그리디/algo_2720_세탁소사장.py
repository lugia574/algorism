import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    coins = [25, 10, 5, 1]
    for _ in range(int(input())):
        money = int(input())
        coinCnt = [0] * 4
        for i in range(4):
            coinCnt[i] = money // coins[i]
            money = money % coins[i]

        print(*coinCnt)
