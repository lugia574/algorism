import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    arr = [i for i in range(1, n+1)]
    res = []
    idx = 0
    for _ in range(n):
        idx += k-1
        if idx >= len(arr):
            idx = idx% len(arr)

        res.append(str(arr.pop(idx)))

    print("<",", ".join(res)[:],">", sep='')