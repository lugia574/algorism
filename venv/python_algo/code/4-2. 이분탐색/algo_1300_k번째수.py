# 그냥 2중 포문해서 값 다 arr 에 박아버리고 sort 해서 k 번째 얘 부르면 답이긴한데
# 근데 이럼 시초가 뜨겠지 ㅋ
# 여기서 굳이 수를 다 구할 필요가 없음
# 특정 수 A 보다 작은 숫자가 몇개인지만 찾으면 A 가 몇번째인지는 바로 알 수 있음 (오른차순으로 한다니까)
# 예를 들어 10 * 10 배열에서 20 보다 작은 수의 갯수를 구했다고 해보자 그때 갯수가 k 번째인지 따져보고
# 맞으면 리턴 아니면 갯수에 따라 20을 줄이거나 올리면 됨
# 그럼 어떻게 구하냐?

# https://velog.io/@uoayop/BOJ-1300-K번째-수Python

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    k = int(input())
    
    lt, rt = 0, k
    # k번째 수는 k보다 클 수 없음
    # 라는데 왜 k 보다 클수 없는지 잘 모르겠는데
    # 대충 추론 해보자면 1X1 이 제법 마니 나옴 이런 짜바리 놈들이 아래 다 깔려서 절대로 k 보다 높은 수는 나오지 않는다 이런 소린가?

    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 0
        for i in range(1, n+1):
            cnt = min(mid//i, n)

        if cnt >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)