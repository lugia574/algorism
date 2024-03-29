# 단어 찾기
# 쓰일 단어를 미리 노트에 적어둡니다.
# 이번에는 N개의 단어를 노트에 적었는데 쓰지 않은 단어가 하나 있다고 합니다.
# 그걸 찾아 주세요
# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
# 두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에
# 쓰인 N-1개의 단어가 주어진다.
# ▣ 출력설명
# 첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.
# ▣ 입력예제 1
# 5
# big
# good
# sky
# blue
# mouse
# sky
# good
# mouse
# big
# ▣ 출력예제 1
# blue
from collections import deque

def notPoetryWord (w, pw):
    w = deque(w)
    pw = deque(pw)

    while pw:
        tmp = w.popleft()
        if pw[0] == tmp:
            pw.popleft()
        else:
            w.append(tmp)

    return w[0]

def inputFnc():
    n = int(input())
    words = []
    PoetryWords = []

    for _ in range(n):
        words.append(input())

    for _ in range(n-1):
        PoetryWords.append(input())

    return n, words, PoetryWords

N, words, PoetryWords = inputFnc()

res =notPoetryWord(words,PoetryWords)

print(res)
