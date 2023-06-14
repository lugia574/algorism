import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, l = map(int, input().rsplit())
    line = list(map(int, input().rsplit()))
    line.sort()
    cut = line[0] + l - 1
    cnt = 1
    for i in range(1, n):
        if cut < line[i]:
            cut = line[i] + l - 1
            cnt += 1

    print(cnt)