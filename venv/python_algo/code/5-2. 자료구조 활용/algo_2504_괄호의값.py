import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    arr = input().rstrip()
    stack = []
    cal = 1
    answer = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
            cal *= 2
        elif arr[i] == '[':
            stack.append(arr[i])
            cal *= 3
        elif arr[i] == ')':
            if not stack or stack[-1] == '[':
                answer = 0
                break
            if arr[i-1] == '(':
                answer += cal
            cal //= 2
            stack.pop()
        else:
            if not stack or stack[-1] == '(':
                answer = 0
                break
            if arr[i-1] == '[':
                answer += cal
            cal //= 3
            stack.pop()
    if stack:
        print(0)
    else:
        print(answer)