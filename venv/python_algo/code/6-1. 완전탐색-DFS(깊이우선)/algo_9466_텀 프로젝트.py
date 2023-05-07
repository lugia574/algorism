# https://kyun2da.github.io/2021/04/29/termProject/
# 내가 한 방법이랑 좀 유사해

# https://bcp0109.tistory.com/32
# 자바는 이걸 참고하도록 합시다
#
# 1->3->3
# 2->1->3->3
#
# 3->3
#
# 어디서 시작해도 끝은 항상 싸이클입니다.
# 이 점을 이용한다면 1, 2, 3 번 노드를 모두 탐색 할 필요 없이 1번 노드 탐색만으로도 싸이클을 만난다는 사실을 알 수 있습니다.
# 그렇다면 2번과 3번 노드는 끝까지 탐색할 필요가 없게 됩니다.
# 그러네 유레카네 이걸 참고해서 하면 될듯?

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


