def solution(s):
    answer = []
    stack = []
    cntA = 0
    cntB = 0
    for i in s:
        if len(stack) == 0:
            stack.append(i)
            cntA += 1
            continue
        if stack[0] == i:
            cntA += 1
        else:
            cntB += 1

        stack.append(i)
        if cntA == cntB:
            answer.append(stack)
            stack = []
            cntA, cntB = 0, 0

    if len(stack) > 0: answer.append(stack)
    print(answer)
    return len(answer)

if __name__ == "__main__":
    s = "banana"
    res = 3
    answer = solution(s)
    print(res == answer, answer)