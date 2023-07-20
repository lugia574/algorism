# https://foramonth.tistory.com/13
# 생각을 해보자
# minpoint 라고 써져 있길래 이게 먼소린가 했음
# 근데 그냥 index임
# 왼쪽부터 한칸씩 가면서 앞에 놈이 현재 스택에 있는 놈보다 큰지만 따져
# 크면 무조건 왼쪽놈 높이 만큼 직사각형이 형성 될테니까
# 가령 1, 4, 6 가 스택에 들어가 있다고 치고 이번에는 개 작은 1 이 왔다고 쳐
# 그럼 6보다 작으니까 현재 비교 대상인 1 의 index 랑 6이 있던 index 랑 빼고 6만큼 곱하면 됨 (1_index - 6_index)
# 당연히 6 다음에 나온 1 이니까 빼면 1 이겠지 그럼 6 * 1 이 되겠지
# 6을 처리했다 치고 그럼 4 를 보자
# (1_index - 4_index) 하면 뭐 2 가 되겠지 그럼 4 * 2 해서 8 이 되는거야

# 그럼 이번에는 1, 4, 6 스택 상태에서 5, 1 이 들어 온다고 해봐
# (5_index - 6_index) 해서 6 나오는건 똑같고
# 4 는 5 가 더 큰거자너 그럼 그냥 더 안빼고 스택에 5를 넣어
# 그럼 1, 4, 5 가 되겠지 그 상태에서 1 이 오니까 아까 위 처럼 각각 index 빼주고 차이 만큼 곱해주고 해주는거임

# 원리 자체는 안어려움 근데 이걸 구현할 머리빡이 안된다
# 근데 이건 세그먼트 트리가 아닌거 같은데
# 자료구조에 더 가까운듯
import sys

def maxSize():
    answer = 0
    stack = []

    for i in range(n):
        idx = i
        while stack and stack[-1][0] >= arr[i]:
            h, idx = stack.pop()
            tmpSize = h * (i-idx)
            answer = max(answer, tmpSize)
        stack.append([arr[i], idx])

    for h, i in stack:
        answer = max(answer, (n-i) * h)

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    while True:
        n, *arr = map(int, input().split())
        if n == 0: break
        res = maxSize()
        print(res)



