import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    group = set()
    cnt = 0
    for _ in range(n):
        s = input()
        group.add(s)

    for _ in range(m):
        ss = input()
        if ss in group:
            cnt += 1

    print(cnt)_