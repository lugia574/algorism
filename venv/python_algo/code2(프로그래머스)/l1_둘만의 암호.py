# 아 이거 개귀찮은데?? ㅋㅋ
# 이것도 dic 만들어서 하는게 맞는거 같긴 한데

def solution(s, skip, index):
    answer = ''
    dic = {}
    for al in s:
        if al in dic:
            answer += dic[al]
            continue
        cnt = 0
        charNum = ord(al)
        while cnt < index:
            if charNum +1 > 122: charNum = 96
            if chr(charNum+1) not in skip:
                cnt += 1
            charNum += 1

        dic[al] = chr(charNum)
        answer += dic[al]
    return answer

if __name__ == "__main__":
    s = "aukks"
    skip = "wbqd"
    index = 5
    res = "happy"
    answer = solution(s, skip, index)
    print(res == answer, answer)