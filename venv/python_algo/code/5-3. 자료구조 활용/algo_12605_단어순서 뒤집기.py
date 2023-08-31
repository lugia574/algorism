import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [list(map(str, input().strip().split(" "))) for _ in range(n)]
    for idx, st in enumerate(arr):
        length = len(st)
        res = ""
        for i in range(length-1, -1 , -1):
            res += "".join(st[i])
            res += " "
        print("Case #%d: %s"%(idx+1, res))