import sys

def gcd(x, y):
    if x == 1 or y == 1:
        return 1
    if x < y:
        x, y = y, x

    while y > 0:
        tmp = x % y
        x = y
        y = tmp

    return x

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        a, b = map(int, input().split())
        gcdNumber = gcd(a, b)
        print(a * b // gcdNumber)
