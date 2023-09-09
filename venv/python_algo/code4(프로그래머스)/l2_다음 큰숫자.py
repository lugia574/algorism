# 캬 똑똑하네 이럼 시복 N 으로 걍 끝나는거자너
# 난 뭐 2진법으로 어떻게 해야하나 했는데 bin 라이브러리는 또 첨 보네 ㅅㅂ
# 내가 너무 부족한게 너무 너무 너무 많다
def solution(n):
    answer = 0
    oneCounter = bin(n).count("1")
    for i in range(n+1,  1_000_000):
        cnt = bin(i).count("1")
        if oneCounter == cnt:
            answer = i
            break
    return answer


if __name__ == "__main__":
    answer = solution(78)
    res = 83
    print(answer == res)

    answer = solution(15)
    res = 23
    print(answer == res)