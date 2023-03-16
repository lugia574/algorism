# 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 3 ≤ L ≤ C ≤ 15
import sys
from itertools import combinations


if __name__ == "__main__":
    input = sys.stdin.readline
    length, c = map(int, input().split())
    alp = list(map(str, input().split()))
    alp.sort()
    words = combinations(alp, length)

    for w in words:
        vowel = 0
        for i in w:
            if i in "aeiou":
                vowel += 1
        if vowel > 0 and length - vowel > 1:
            print("".join(w))


# def backTrack(l, idx):
#     if l == length:
#         co, vo = 0,0
#         for w in word:
#             if w in "aeiou":
#                 vo += 1
#             else:
#                 co += 1
#         if co > 1 and vo >= 1:
#             print("".join(word))
#         return
#     else:
#         for i in range(idx, c):
#             word.append(alp[i])
#             backTrack(l + 1, idx + 1)
#             word.pop()
