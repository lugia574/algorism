# 알파코드(DFS)
# 영희 : 우리 알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당하여 번호로 보내기로 하자.
# 철수 : 정말 바보같은 생각이군!! 생각해 봐!! 만약 내가 “BEAN"을 너에게 보낸다면 그것을 암
# 호화하면 25114이잖아!! 이것을 알파벳으로 바꾸면 BEAAD, YAAD, YAN, YKD 그리고 BEKD로 BEAN말고도 5가지나 더 있군.
# 당신은 위와 같은 영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데
# 얼마나 많은 방법인 있는지 구하세요.
# ▣ 입력설명
# 첫 번째 줄에 숫자로 암호화된 코드가 입력된다. (코드는 0으로 시작하지는 않는다, 코드의 길
# 이는 최대 50이다) 0이 입력되면 입력종료를 의미한다.
# ▣ 출력설명
# 입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력한다. 그 가지
# 수도 출력한다. 단어의 출력은 사전순으로 출력한다.
# ▣ 입력예제 1
# 25114
# ▣ 출력예제 1
# BEAAD
# BEAN
# BEKD
# YAAD
# YAN
# YKD
# 6
def translate(l):
    if l == n:
        char =""
        for i in cha:
            tmp = chr(i + 64)
            char+=tmp
        res.append(char)

    else:
        for i in range(1, 27):
            if i < 10:
                if i == code[l]:
                    cha.append(code[l])
                    translate(l + 1)
                    cha.pop()
            else:
                if l+1 < n:
                    if i == (code[l] * 10) + code[l+1]:
                        tmp = (code[l] * 10) + code[l+1]
                        cha.append(tmp)
                        translate(l + 2)
                        cha.pop()
if __name__ == "__main__":
    code = list(map(int,input()))
    n = len(code)
    cha = []
    res = []

    translate(0)

    for i in res:
        print(i)
    print(len(res))