def solution(s):
    answer = []
    s_list = list(map(int, s.replace("{", "").replace("}", "").split(",")))

    number = {}
    for i in s_list:
        if i not in number:
            number[i] = 1
        else:
            number[i] += 1

    snum = sorted(number.items(), key=lambda x: x[1], reverse=True)
    for k in snum:
        answer.append(k[0])

    return answer


if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    res = [2, 1, 3, 4]
    answer = solution(s)
    print(res == answer, answer)

    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    res = [2, 1, 3, 4]
    answer = solution(s)
    print(res == answer, answer)

    s = "{{20,111},{111}}"
    res = [111, 20]
    answer = solution(s)
    print(res == answer, answer)

    s = "{{123}}"
    res = [123]
    answer = solution(s)
    print(res == answer, answer)

    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    res = [3, 2, 4, 1]
    answer = solution(s)
    print(res == answer, answer)