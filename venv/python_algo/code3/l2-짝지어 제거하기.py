# 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다
def solution(s):
    arr = list(s)
    tmp = ["zero"]
    for i in arr:
        if tmp[-1] == i:
            tmp.pop()
        else:
            tmp.append(i)

    if len(tmp) == 1:
        return 1
    return 0

if __name__ == "__main__":
    s = "baabaa"
    result = 1

    res = solution(s)
    print("True" if res == result else "False")

    s = "cdcd"
    result = 0

    res = solution(s)
    print("True" if res == result else "False")