# 약간 먼가 이해가 안가는데??
# 현재 대기열의 사람들은 이 공간으로 올 수 있지만 반대는 불가능하다
# 라는게 대기열에서 사람 갈순 있어고 따로공간에서 대기열로는 못간다는 소리야?
# 아하아하아항 생각이 멍청했다
# 단순히 먼저 큐 부분을 먼저 처리해야한다고 생각해버렷어 이러면 안돼
# 가령 5 4 2 1 3 이였다고 해봐 그럼 5, 4, 2 까지는 스택에 넣어버리고 1에서 popleft 가 되어 버릴꺼 아녀
# 그럼 이제 스택에 있는 2를 조져야하는데 내가 처음에 짠 코드대로면 3 을 스택에 박아 넣고 큐 다 쓴 다음에 그담에 스택을 털어
# 이러면 스택이 5, 4, 2, 3 상태라 제대로 뽑아낼수 없는 상황이 되버리징 이래서 틀린거
# 방법은 매 큐를 할때마다 스택에 맨 윗값을 보고 스택 털수 있을때 털어버려야하는거임 ㅇㅇㅇㅇㅇㅇㅇㅇ

import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    queue = deque(map(int, input().split()))
    stack = deque()
    i = 1
    while queue:
        if queue and queue[0] == i:
            queue.popleft()
            i += 1
        else:
            stack.append(queue.popleft())
        while stack and stack[-1] == i:
            stack.pop()
            i += 1

    print("Nice" if not stack else "Sad")