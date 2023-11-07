# 세상에 이렇게 쉬울수가가가가가!~ 너무 빨리 풀어버렸는데~
def solution(lottos, win_nums):
    lotto = 0
    zero = 0
    for l in lottos:
        if l == 0:
            zero += 1
        elif l in win_nums:
            lotto += 1
    minRank = 7 - lotto if lotto > 0 else 6
    maxRank = 7 - (lotto + zero) if (lotto + zero) > 0 else 6
    return [maxRank, minRank]

if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    res = [3, 5]
    answer = solution(lottos, win_nums)
    print(res == answer, answer)

    lottos = [0, 0, 0, 0, 0, 0]
    win_nums = [38, 19, 20, 40, 15, 25]
    res = [1, 6]
    answer = solution(lottos, win_nums)
    print(res == answer, answer)

    lottos = [45, 4, 35, 20, 3, 9]
    win_nums = [20, 9, 3, 45, 4, 35]
    res = [1, 1]
    answer = solution(lottos, win_nums)
    print(res == answer, answer)
