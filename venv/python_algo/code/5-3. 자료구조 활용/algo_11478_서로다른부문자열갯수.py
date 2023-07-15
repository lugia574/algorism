# 조합 만들기
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    st = list(input().strip())
    n = len(st)
    s = set()
    for i in range(n):
        for j in range(i+1, n+1):
            s.add(''.join(st[i:j]))
    print(len(s))
