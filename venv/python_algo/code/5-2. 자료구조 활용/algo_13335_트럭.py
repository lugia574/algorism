# 이거 전형적인 큐 문제 아닌가?
# 이게 쉬운데 못풀었음
# 내가 구현 능력이 후달리다는 증거지
# 여기서 핵심은 다리 길이를 어떻게 구현 할것인가임
# 단순히 트럭에다가 얼만큼 갔냐 하고 시간 변수를 추가하면 오히려 복잡해짐
# 이때는 간단하게 그냥 deque 로 다리 길이만큼 0 을 줘버리면 되는거임
# 가령 길이가 2인 다리다 하면 00 이렇게 하고 popleft 해줘서 하나씩 앞에서 빼고 뒤로 하나씩 박는거임
# 만약에 07 인 상태고 다리 무게가 10 까지인데 뒤에 오는 무게가 4 다?
# 그럴경우 그냥 다시 0 을 박으면 됨
# 그럼 이런식으로 진행이 됨 07 >> 70 >> 04 >> 4X... 이런식으로

import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n, w, l = map(int, input().split())
    arr = deque(map(int, input().split()))
    bridge = deque([0 for _ in range(w)])
    time = 0
    while bridge:
        time += 1
        bridge.popleft()
        if not arr: continue
        if sum(bridge) + arr[0] <= l:
            bridge.append(arr.popleft())
        else:
            bridge.append(0)
    print(time)