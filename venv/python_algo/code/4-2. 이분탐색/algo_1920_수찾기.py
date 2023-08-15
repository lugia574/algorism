# 그냥 수의 범위까지 쭈욱 배열을 초기화하고
# 해당 값을 index 로 써서 1 로 표시하고 그대로 배열 index를 부르면 되지 않을까 했는데
# 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31 로 존나 커서 안됨 ㅋㅋ
# 그래서 이분탐색을 쓰는거임 ㅋ
# 먼저 arr 를 sort 해주고
# 0, n-1 의 중간값을 구해서 그것보다 큰지 작은지 업 다운을 갈겨주면서
# 범위 좁혀 나가면 됨
# 그러다가 num 이 있다 하면 1 출력해주고 break 해주고
# 없으면 쭈욱 돌다가 lt 가 rt 를 넘어가게 되면서 끝나고  0 출력해주면 되는거임

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    mArr = list(map(int, input().split()))

    arr.sort()

    for num in mArr:
        lt, rt = 0, n - 1
        isExist = False

        while lt <= rt:
            mid = (lt + rt) // 2
            if num == arr[mid]:
                isExist = True
                print(1)
                break
            elif num > arr[mid]:
                lt = mid + 1
            else:
                rt = mid - 1

        if not isExist:
            print(0)