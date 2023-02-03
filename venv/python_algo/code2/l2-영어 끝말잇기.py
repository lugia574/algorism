
from collections import deque

def solution(n, words):
    dq = deque(words)
    answer = []
    roundCount = 1
    dic = {}
    prevWorad = words[0][0]
    breakBool = False
    while dq:
        if breakBool:
            break

        for i in range(n):
            if breakBool:
                break

            word = dq.popleft()
            if word[0] != prevWorad:
                answer = [i + 1, roundCount]
                breakBool = True
            if word in dic:
                answer = [i + 1, roundCount]
                breakBool = True
            else:
                dic[word] = i + 1
                prevWorad = word[-1]

        roundCount += 1

    if not answer:
        answer = [0, 0]

    return answer


if __name__ == "__main__":
    n = 3
    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    result = [3, 3]

    n2 = 5
    words2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    result2 = [0, 0]

    n3 = 2
    words3 = ["hello", "one", "even", "never", "now", "world", "draw"]
    result3 = [1, 3]

    res = solution(n, words)
    res2 = solution(n2, words2)
    res3 = solution(n3, words3)

    print(res)
    print(res2)
    print(res3)
    print("정답입니다." if res == result else "틀렸습니다 모지리새끼야")
    print("정답입니다." if res2 == result2 else "틀렸습니다 모지리새끼야")
    print("정답입니다." if res3 == result3 else "틀렸습니다 모지리새끼야")