import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    idx = 1
    while True:
        l, p, v = map(int, input().split())
        # if l == 0 and p == 0 and v == 0:
        #     break
        if l + p + v == 0:
            break

        res = (v//p)* l
        res += min((v%p), l)
        print("Case {}: {}".format(idx, res))
        idx += 1
