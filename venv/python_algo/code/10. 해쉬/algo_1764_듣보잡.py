import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    notHeard = {}
    res = []
    for _ in range(n):
        notHeard[input().strip()] = 1

    for _ in range(m):
        notSeen = input().strip()
        if notSeen in notHeard:
            res.append(notSeen)
    res.sort()
    print(len(res))
    for x in res:
        print(x)
