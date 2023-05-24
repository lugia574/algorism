# 이거 파이썬으로는 별거 아닌데 자바로는 어떻게 해야할지를 모르겠네

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    strArr = input().rstrip()
    bomb = input().rstrip()
    length = len(bomb)
    stack = []

    for i in range(len(strArr)):
        stack.append(strArr[i])
        if ''.join(stack[-length:]) == bomb:
            for _ in range(length):
                stack.pop()
    print(''.join(stack) if stack else "FRULA")
