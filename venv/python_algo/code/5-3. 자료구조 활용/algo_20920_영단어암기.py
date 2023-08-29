# 빈도 높은순으로, 길이 순으로, 알파벳 순으로
# 길이 M 이상의 단어들만
# 음
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    data = {}
    for _ in range(n):
        word = input().strip()
        wordLength = len(word)
        if wordLength < m: continue
        if word in data:
            data[word] += 1

        else:
            data[word] = 1
    # 이렇게 정렬을 하라는 거시다~
    sorted_data = sorted(data.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

    for key, item in (sorted_data):
        print(key)