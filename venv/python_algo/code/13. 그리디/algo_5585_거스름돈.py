import sys

def changeFnc(cost):
    changeList = [500, 100, 50, 10, 5, 1]
    money = 1000
    coin = 0
    if cost == money:
        return coin
    money -= cost
    for c in changeList:
        coin += money // c
        money = money % c
    return coin

if __name__ == "__main__":
    input = sys.stdin.readline
    cost = int(input())
    res = changeFnc(cost)
    print(res)