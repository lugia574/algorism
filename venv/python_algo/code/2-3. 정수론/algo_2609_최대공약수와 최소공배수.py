# 최대 공약수 >> 유클리드 호제법 호제야!~
# 최소 공배수 >> a * b // 최대 공약수  호예야!~

import sys

def gcd(x, y):
    if x < y:
        x, y = y, x

    while y > 0:
        tmp = x % y
        x = y
        y = tmp

    return x

if __name__ == "__main__":
    input = sys.stdin.readline
    a, b = map(int, input().split())

    gcdNum = gcd(a, b)
    print(gcdNum)
    print(a*b//gcdNum)