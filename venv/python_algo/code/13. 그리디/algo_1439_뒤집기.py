# https://hazung.tistory.com/116
# 설명하자면 00001이나 01이나 바꾸는 횟수는 똑같음 1번임
# 아무리 많은 문자열이 있다한들 같은 문자들은 사실상 하나의 문자랑 같다는 소리지
# 그러니까 01 처럼 다른 문자열이 되는 순간을 카운팅 해
# 단순히 카운팅만 해서는 안됨
# 여기서 010 이여도 바꾸는 횟수는 1이야
# 0101 총 4개가 번갈아 달라야지 횟수가 2가 되는거야
# 즉 카운팅 갯수 + 1 // 2 해줘야 하는거 <<< +1 해주는 이유는 0101 에서 맨 처음 0은 감지를 못하니까 카운팅이 딱 3만 됨

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    S = input().rstrip()
    count = 0
    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            count += 1
    print((count + 1) // 2)