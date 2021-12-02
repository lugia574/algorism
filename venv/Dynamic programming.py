# 동적 프로그래밍

# 피보나치 수열

def fibo (N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    else:
        return fibo(N-1) + fibo(N-2)


############################################
############################################

fibo_arr = [0, 1]
def fibo_top (n):
    if n < len(fibo_arr):
        return fibo_arr[n]
    else:
        fib = fibo_top(n-1) + fibo_top(n-2)
        fibo_arr.append(fib)
        return fib


############################################
############################################

def fibo_bt(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fibo_arr2 = [0, 1]
    for i in range(2, n + 1):
        num = fibo_bt(i-1) + fibo_bt(i-2)
        fibo_arr2.append(num)

    return fibo_arr2(n)

############################################
############################################

# 계단 오르기




