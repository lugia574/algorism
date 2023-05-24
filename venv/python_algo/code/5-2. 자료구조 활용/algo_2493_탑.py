# 어떻게 돌아가는지 설명을 해줄꼐
# 자 단순히 2중 포문으로 하면 연산이 대충 2억이 넘어가서 못해도 2초는 필요해
# 그래서 스택을 쓴데
# while 은 스택을 가지고 있을 경우에만 돌아가니까 무조건 처음에는 그대로 지나치고 스택에 값을 넣을 수 밖에 없어
# 자 i=1 부터는 스택이 있지? 여기서 만약에 지금 값이랑 스택 맨위 값이랑 비교해서 만약에 지금값이 더 크다?
# 문제는 신호를 쏠때 맞을려면 (왼쪽으로) 좀 더 커야하는거자나 그니까 현재 스택 건물은 안닿는거지
# 글고 지금 건물값이 더 크다는건 앞으로의 건물들이 어떻게 되든 stack 맨위 값의 건물은 닿을리가 없겠지
# 그러니까 맨위 값을 pop 해버려 그리고 계속 스택에 지금 값보다 큰 스택을 찾아
# 찾으면 answer 에 기록하고 pop 하지 않고 그대로 break
# 이걸 쭉 도는거야
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    towers = list(map(int, input().split()))
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack:
            if stack[-1][1] < towers[i]:
                stack.pop()
            else:
                answer[i] = stack[-1][0] + 1
                break
        stack.append((i, towers[i]))
    print(*answer)