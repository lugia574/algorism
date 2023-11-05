# 아 개 귀찮네
# 뭔소리야 이런 시벌
# 어떻게 해야할지 모르겠는데??????
# 안나올때까찌 쭉 N 순회 돌리라고????
# 안돼 그라면 안돼 ingredient의 길이 ≤ 1,000,000 이런데
# 무조건 한번 순회때 끝내야함 그럼 스택으로 해야할꺼 가튼데
# stack으로 했다잉 잇힝~ if size < 4: continue 요고 범위 잘못줘서 한참을 고생했네~~
def solution(ingredient):
    buger = (1, 2, 3, 1)
    answer = 0
    stack = []
    size = 0
    for i in ingredient:
        stack.append(i)
        size +=1
        if size < 4: continue
        ok = True
        for i in range(1, 5):
            if stack[size - i] != buger[4 - i]:
                ok = False
                break
        if ok:
            for i in range(4):
                stack.pop()
            size -= 4
            answer += 1
    return answer

if __name__ == "__main__":
    ingredient = [1, 2, 3, 1, 2, 3, 1, 1]
    res = 2
    answer = solution(ingredient)
    print(res == answer, answer)

    ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
    res = 2
    answer = solution(ingredient)
    print(res == answer, answer)

    ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
    res = 0
    answer = solution(ingredient)
    print(res == answer, answer)