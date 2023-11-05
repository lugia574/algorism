# 띠용 먼가 오래 걸리고 고생할줄 알았는데
# 쉽게 풀려버리네

def solution(keymap, targets):
    dic = {}
    answer = []
    for target in targets:
        cnt = 0
        for t in target:
            if t in dic:
                cnt += dic[t]
                continue
            minCnt = 101
            for key in keymap:
                if t in key:
                    minCnt = min(key.index(t) + 1, minCnt)

            # keymap 에 없다는 소리
            if minCnt == 101:
                cnt = -1
                break
            dic[t] = minCnt
            cnt += minCnt

        answer.append(cnt)

    return answer

if __name__ == "__main__":
    keymap = ["ABACD", "BCEFD"]
    targets = ["ABCD","AABB"]
    res = [9, 4]
    answer = solution(keymap, targets)
    print(res == answer, answer)

    keymap = ["AA"]
    targets = ["B"]
    res = [-1]
    answer = solution(keymap, targets)
    print(res == answer, answer)

    keymap = ["AGZ", "BSSS"]
    targets = ["ASA","BGZ"]
    res = [4, 6]
    answer = solution(keymap, targets)
    print(res == answer, answer)