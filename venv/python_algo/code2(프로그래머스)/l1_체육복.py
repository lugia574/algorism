# 와 드디어 풀었다 ㅋㅋㅋㅋ
# 개 쉬운데 이걸 못풀어서 존나 낑낑됨
# ㄹㅇ 개 직관적으로 n 배열 만들어서 3n, 4n 으로 반복문 돌리면 시초 걸려서 안되고
# 그렇다고 remove 함수로 요소 찾아서 지워서 하는 식으로 하면 배열 꼬여서 개판나고
# 아 이걸 어쩌지 하다가 두개 섞어서 함

def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()

    s = [0] * (n + 1)
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            s[l] = -1
            answer -= 1

    for r in reserve:
        if r - 1 > 0 and s[r - 1] == -1:
            s[r - 1] += 1
            answer += 1

        elif r + 1 < n + 1 and s[r + 1] == -1:
            s[r + 1] += 1
            answer += 1

    return answer

if __name__ == "__main__":
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    res = 5
    answer = solution(n, lost, reserve)
    print(res == answer, answer)

    n = 5
    lost = [2, 4]
    reserve = [3]
    res = 4
    answer = solution(n, lost, reserve)
    print(res == answer, answer)


    n = 3
    lost = [3]
    reserve = [1]
    res = 2
    answer = solution(n, lost, reserve)
    print(res == answer, answer)