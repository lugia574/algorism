# https://velog.io/@joniekwon/Python-백준-2812번-크게-만들기
# 흠 나는 dfs 로 가지치기 해서 풀어야하나 했어
# 근데 딱봐도 터지거나 할꺼 같았는데
# 아니나다를까 메모리 초과 됐어
# 그래서 검색해보니까 스택으로 하나씩 넣으면서 다음에 넣을 값이 더 크다
# 그럼 스택에 더 클놈이 나올때까지 pop 해줘 그게 k 번까지만
# 그렇게 다 들어가면 이때 k 번까지 다 pop 안했을수도 있음
# 그러니까 k>0 이면 stack[:-k] 까지 출력해주고
# k == 0 이면 stack 다 출력해주면 됨

import sys
# sys.setrecursionlimit(int(1e9))

if __name__ == "__main__":
    input = sys.stdin.readline

    n, k = map(int, input().split())
    numbers = input().rstrip()
    stack = []
    for number in numbers:
        while stack and stack[-1] < number and k > 0:
            stack.pop()
            k -= 1
        stack.append(number)
    if k > 0:
        print(''.join(stack[:-k]))
    else:
        print(''.join(stack))


# def dfs(l, x, st):
#     global maxNum
#     if l == n - k:
#         maxNum = max(int(st), maxNum)
#         return
#     for y in range(x+1, n):
#         dfs(l+1, y, st + arr[y])
#
# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n, k = map(int, input().split())
#     arr = list(map(str, input().strip()))
#     maxNum = 0
#
#     for i in range(n-k):
#         dfs(1, i, arr[i])
#
#     print(maxNum)