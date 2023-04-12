import sys

def printQue(n, m, val):
    q = []
    for i in range(n):
        q.append([i, val[i]])
    cnt = 0
    point = max(val)

    while q:
        tmp = q.pop(0)
        if tmp[1] == point:
            cnt += 1
            val.remove(point)
            if tmp[0] == m:
                break
            point = max(val)
        else:
            q.append(tmp)
    return cnt

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        val = list(map(int,input().split()))
        res = printQue(n, m, val)
        print(res)