import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    d = dict()
    for _ in range(n):
        name, e = input().strip().split(".")
        if e in d:
            d[e] += 1
        else:
            d[e] = 1

    keys = sorted(d.keys())

    for k in keys:
        print(k, d[k])
