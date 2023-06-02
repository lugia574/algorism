# https://velog.io/@yanghl98/백준-2407-조합-JAVA자바 
# 이거 신기하다 BigInteger 를 씀 ㅋ
# BigInteger : 문자열 형태로 이루어져 있어 숫자의 범위가 무한
import sys, math
def fact ():
    n, m = map(int, input().split())
    up = math.factorial(n)
    down = (math.factorial(n - m)) * (math.factorial(m))
    print(up // down)
    
def combin(x, y):
    n = 1
    r = 1
    for i in range(y): n *= (x - i)
    for j in range(1, y + 1): r *= j
    return (n // r)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int,input().split())
    res = combin(n, m)
    print(res)