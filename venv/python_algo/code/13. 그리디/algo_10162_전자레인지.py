import sys

def microW(t):
    timer = [300, 60, 10]
    arr = []
    if t % 10 != 0:
        return arr

    for i in range(3):
        arr.append(t // timer[i])
        t = t % timer[i]
    return arr
if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    res = microW(t)
    if res:
        print(*res)
    else:
        print(-1)
