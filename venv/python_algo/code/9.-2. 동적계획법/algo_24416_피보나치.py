def fib(n):
    global fibCnt

    if n == 1 or n == 2:
        return 1
    else:

        return fib(n-1) + fib(n - 2)

def dyFib(n):
    global byFibCnt

    if f[n] != 0:
        return f[n]
    else:
        byFibCnt += 1
        f[n] = dyFib(n-1) + dyFib(n-2)
        return f[n]


if __name__ == "__main__":
    n = int(input())
    f = [0] * (n + 1)

    f[1],f[2] = 1, 1

    fibCnt, byFibCnt = 0, 0

    res = fib(n)
    res2 = dyFib(n)

    print(res, byFibCnt)
