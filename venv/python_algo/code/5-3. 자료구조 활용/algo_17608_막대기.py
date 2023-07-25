import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    vb = 0
    cnt = 0
    for i in range(n-1, -1, -1):
        if vb < arr[i]:
            vb = arr[i]
            cnt += 1
    print(cnt)