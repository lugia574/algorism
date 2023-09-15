# 이거 단순히 2중 포문으로 하면 안됨

import sys
sys.setrecursionlimit(int(1e9))
def DFS(l, com):
    if l == k:
        numSet.add(com)
        return
    for i in range(n):
        if check[i]: continue
        check[i] = True
        DFS(l+1, com+str(card[i]))
        check[i] = False

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    k = int(input())
    card = [int(input()) for _ in range(n)]
    numSet = set()
    check = [False] * n

    for i in range(n):
        check[i] = True
        DFS(1, str(card[i]))
        check[i] = False

    print(len(numSet))
