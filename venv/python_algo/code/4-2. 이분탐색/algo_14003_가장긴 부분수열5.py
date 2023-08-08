# https://onn5.tistory.com/37 이걸 보도록 하자
# 코드를 보니까 이해가 안가네
# 이 코드는 dp 에 index 값까지 같이 저장하는 형식이거든?
# 그리고 그걸 이제 역순으로 돌면서 값을 찾는 식으로 하는건데
# 내가 binary 하면서 바로바로 값을 넣는거랑 뭔 차이지?
# 내가한건 틀리고 이건 맞음?
# 대충 보니까 그러면 뭐가 문제냐면
# 답은 1, 3, 5, 9 막 이래야하는데
# 나오는 답읍 1, 2, 5, 9 막 이럴 수 있다는거야~
# 흐으음~ 여튼 그렇다~ 나중에 다시 봐야할듯 솔직히 지금 내가 공부에 머리가 제대로 안들어감
# 자꾸 지금 마음은 딴곳에 가 있음 집에 가도 뭐 할것도 없는데 말이야

def binarySearch(e):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1

    return start


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    LIS = [arr[0]]
    # dp에는 LIS에 들어간 인덱스를 저장해둔다.
    dp = [(0, arr[0])]

    for i in range(1, n):
        if arr[i] > LIS[-1]:
            LIS.append(arr[i])
            dp.append((len(LIS) - 1, arr[i]))

        else:
            idx = binarySearch(arr[i])
            LIS[idx] = arr[i]
            dp.append((idx, arr[i]))

    print(len(LIS))

    # 역추적
    last_idx = len(LIS) - 1
    res = []
    for i in range(len(dp) - 1, -1, -1):
        # i번째 값의 index와 마지막 인덱스값과 같다면
        if dp[i][0] == last_idx:
            res.append(dp[i][1])
            last_idx -= 1

    print(*res[::-1])

