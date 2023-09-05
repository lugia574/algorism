import sys

def wordReverse(l, word):
    answer = ""
    for i in range(l-1, -1, -1):
        answer += word[i]
    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    wordSet = set()

    for _ in range(n):
        word = input().strip()
        length = len(word)
        reWord = wordReverse(length, word)
        if word in wordSet or reWord in wordSet or word == reWord:
            print(length, end= " ")
            print(word[length//2])
            break

        wordSet.add(word)
        wordSet.add(reWord)