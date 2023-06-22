# 아 나는 그냥 양쪽에 하나하나 박는걸 생각했는데 너무 바보같은 생각이야
# 그냥 쓸데없이 복잡하기만하고 실효성같은건 없음 ㅋㅋ
# 짝수든 홀수든 절반을 기준으로 보면 앞문자와 뒷문자가 똑같음
# 그니까 앞문자열만 완성하고 뒷문자열은 리버스해서 붙혀버리면 됨
# 홀수의 경우는 앞문자열 + 홀수문자 + 뒷문자열 이렇게 해버리면 됨

# 는 틀렸네 뭔데 시벌 ㅋ 어디가 잘못됏는데 ㅋㅋ
# 귀찮아서 걍 복붙함

import sys
from collections import Counter

word = list(map(str, sys.stdin.readline().strip()))
word.sort() # 사전순으로 정렬하기 위해 오름차순 정렬
check = Counter(word) # 홀수의 개수를 확인하기 위해 Counter 함수 사용

cnt = 0 # 홀수의 개수
center = "" # 홀수의 문자

for i in check:

    if check[i] % 2 != 0:
        cnt += 1
        center += i
        word.remove(i)
    if cnt > 1:
        break

if cnt > 1:
    print("I'm Sorry Hansoo")

else:

    res = ""
    for i in range(0, len(word), 2):
        res += word[i]

    print(res + center + res[::-1])