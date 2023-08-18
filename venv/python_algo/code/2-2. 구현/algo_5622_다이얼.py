# 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다
# 이게 뭔소리냐 하고 보니까 그림에 써져 있네 ABC 2 DEF 3 이런식으로 근데 이러면 1 은 뭐 어떡함?
# ㅅㅂ 자괴감 드네 ㅋㅋ
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    res = 0
    dic = {"A": 2, "B": 2, "C": 2, "D": 3, "E": 3, "F": 3, "G": 4, "H": 4, "I": 4,
           "J": 5, "K": 5, "L": 5, "M": 6, "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7, "S": 7,
           "T": 8, "U": 8, "V": 8, "W": 9, "X": 9, "Y": 9, "Z": 9}

    for x in list(input().strip()):
        number = dic[x]
        res += number + 1

    print(res)

