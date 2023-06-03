
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    s = int(input())

    n = 1
    while True:
        if (n * (n+1)) / 2 > s:
            break
        else:
            n += 1
    print(n-1)