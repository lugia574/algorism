# https://kyun2da.github.io/2021/04/29/termProject/
# 내가 한 방법이랑 좀 유사해

import sys

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline


def dfs(x):
    global ans
    vis[x] = True
    cycle.append(x)
    num = arr[x]

    if vis[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    vis = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not vis[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))

# import sys
# sys.setrecursionlimit(10 ** 7)
# 
# def dfs():
#     global arr
#     nextNode = nums[arr[-1]-1]
#     if check[nextNode]: return
# 
#     if arr[0] == nextNode:
#         for x in arr:
#             check[x] = True
#     else:
#         if arr[-1] == nextNode: return
#         arr.append(nextNode)
#         dfs()
#     arr.pop()
# 
# if __name__ == "__main__":
#     input = sys.stdin.readline
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         check = [False] * (n+1)
#         cnt = 0
#         for i in range(1, n+1):
#             arr = []
#             if not check[i]:
#                 arr.append(i)
#                 dfs()
#         # print(check)
#         for i in range(1, n+1):
#             if not check[i]:
#                 cnt += 1
#         print(cnt)


