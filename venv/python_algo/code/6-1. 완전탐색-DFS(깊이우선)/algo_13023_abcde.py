# 문제가 abcde 해서 총 5명만 맞으면 되네 n 으로 몇명이 쳐 있든 조건에 맞는 5명만 있으면 되는거였어 ㅋㅋㅋㅋ
import sys

def DFS(l, idx):
    global ok
    if l == 4:
        ok = True
    else:
        for x in node[idx]:
            if visited[x] == 0:
                visited[x] = 1
                DFS(l+1, x)
                visited[x] = 0

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().rsplit())
    node = [[] for _ in range(n)]
    ok = False
    visited = [0] * n
    for _ in range(m):
        a, b = map(int, input().rsplit())
        node[a].append(b)
        node[b].append(a)

    for i in range(n):
        visited[i] = 1
        DFS(0, i)
        visited[i] = 0
        if ok:
            break
    print(1 if ok else 0)