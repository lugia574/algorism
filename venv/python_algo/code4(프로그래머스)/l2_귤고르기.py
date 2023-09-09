# 정렬과 딕셔너리가 좀 빡센거 같은데 시벌
# https://velog.io/@minmong/프로그래머스-Lv.2-귤-고르기-Python-velog
# 난 왤캐 기본이 안되있냐 ㅋ

def solution(k, tangerine):
    answer = 0
    dic = dict()
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    arr = dict(sorted(dic.items(), key= lambda x: (x[1], x[0]), reverse= True))
    
    for i in arr:
        if k <= 0:
            return answer
        k -= arr[i]
        answer += 1

    return answer


if __name__ == "__main__":
    k = 6
    tangerine =	[1, 3, 2, 5, 4, 5, 2, 3]
    res = 3
    answer = solution(k, tangerine)
    print(res == answer)

    k = 4
    tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
    res = 2
    answer = solution(k, tangerine)
    print(res == answer)

    k = 2
    tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
    res = 1
    answer = solution(k, tangerine)
    print(res == answer)