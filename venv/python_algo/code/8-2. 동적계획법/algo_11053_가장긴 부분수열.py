import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    sequence = list(map(int, input().split()))
    dp = [0] * 1001



    print((dp[:n]))


# 6
# 90 20 90 30 20 50
# 3