import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    lt = 0
    rt = n-1
    answer = abs(a[lt] + a[rt])
    ltNum, rtNum = 0, 0

    while lt < rt:
        tmp = a[lt] + a[rt]

        if abs(tmp) <= answer:
            answer = abs(tmp)
            ltNum = a[lt]
            rtNum = a[rt]

            if answer == 0:
                break

        if tmp < 0:
            lt += 1
        else:
            rt -= 1

    print(ltNum, rtNum)