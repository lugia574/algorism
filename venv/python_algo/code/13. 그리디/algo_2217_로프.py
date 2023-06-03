# 아하 그놈의 정렬
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    rope = [int(input()) for _ in range(n)]
    rope.sort(reverse= True)
    w = []
    for i in range(n):
        w.append(rope[i] * (i+1))
    print(max(w))