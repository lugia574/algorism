# n k >> n! / k! (n-k)!
import sys

def pac(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())

    print(pac(n)// (pac(k) * pac(n-k)))




