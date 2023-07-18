# 난 이게 뭔소린지 이해가 안감
# 만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면, 그 단어는 '좋은 단어'
# 답 보고 유추했는데
# 그냥 자신과 동일한 문자가 나오면 없애고 없앤만큼 밀어서 또 동일하면 없애고
# 딱 stack 형태로 pop 해주는 그런거임

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    res = 0

    for _ in range(n):
        tmp = input().rstrip()
        stack = []
        size = len(tmp)
        for i in range(size):
            if stack and tmp[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(tmp[i])
        if not stack: res += 1

    print(res)