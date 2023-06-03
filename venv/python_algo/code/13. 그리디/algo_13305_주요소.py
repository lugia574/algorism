import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    dist = list(map(int, input().rsplit()))
    city = list(map(int, input().rsplit()))
    res = 0
    m = city[0]
    for i in range(n-1):
        if m > city[i]:
            m = city[i]
        res += m * dist[i]
    print(res)