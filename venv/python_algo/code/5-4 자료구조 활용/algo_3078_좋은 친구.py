# 뭔 문제를 ㄱㅄ같이 낸다
# 흠 단순 반복문 2개 조지는걸로는 타임아웃 나버리네
# k 만큼만 가는거니까 상관없겠거니 했는데 안됨 ㅋ
# 이러면 방법은 queue 를 조져야겠네 염벙벙벙커링 양파링 근데 이게 대체 뭐가 다름??

# 크 이렇게 하니까 반복문 하나만 조지고 쌉가능이네

import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    grade = [0] * 21
    friend = deque()
    cnt = 0

    for _ in range(n):
        name = len(input().strip())
        friend.append(name)
        grade[name] += 1

        friendLen = len(friend)

        if friendLen > k+1:
            old = friend.popleft()
            grade[old] -= 1

        if friendLen > 0:
            cnt += grade[name] - 1

    print(cnt)


