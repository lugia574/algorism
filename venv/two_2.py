answer = -100000;


def solution(paper, n):
    re(paper, n);
    return answer


def re(paper, n):
    global answer
    answer = max(answer, max(paper))
    if n == 0:
        return

    for index in range(len(paper)):
        re(fold_paper(paper, index+1), n - 1)

    return


def fold_paper(paper, index):
    sol = []

    if index > len(paper) // 2:
        right_cnt = len(paper) - index
        for i in range(right_cnt):
            sol.append(paper[index - i - 1] + paper[index + i])
        sol = sol + paper[:index - right_cnt][::-1]

    else:
        for i in range(index):
            sol.append(paper[index - i - 1] + paper[index + i])
        sol = sol + paper[(index * 2):]

    return sol


