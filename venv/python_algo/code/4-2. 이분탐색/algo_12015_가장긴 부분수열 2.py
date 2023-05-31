# 와 dp로 하니까 틀리네 ㅋㅋㅋ
# 이래서 이분탐색으로 하라는 소린가 ㅋㅋ
# https://st-lab.tistory.com/285
import sys

def find(target):
    l, h = 1, len(stack)-1
    while l < h:
        m = (l+h)//2
        if stack[m] < target:
            l = m+1
        elif stack[m] > target:
            h = m
        else:
            l = h = m
    return h

input = sys.stdin.readline()
l = int(input())
arr = list(map(int, input().rsplit()))
stack = [0]

for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[find(a)] = a

print(len(stack)-1)