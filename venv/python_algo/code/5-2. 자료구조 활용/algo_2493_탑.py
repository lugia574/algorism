import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    towers = list(map(int, input().split()))
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack:
            if towers[stack[-1][0]] < towers[i]:
                stack.pop()
            else:
                answer[i] = stack[-1][0] + 1
                break
        stack.append((i, towers[i]))
    print(*answer)