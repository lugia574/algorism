# 창고정리
# 대충 평탄화 작업임

# ▣ 입력설명
# 첫 번째 줄에 창고 가로의 길이인 자연수 L(1<=L<=100)이 주어집니다.
# 두 번째 줄에 L개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 100을 넘지
# 않습니다
# 세 번째 줄에 높이 조정 횟수인 M(1<=M<=1,000)이 주어집니다.
# ▣ 출력설명
# M회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이를 출력하세요.
# ▣ 입력예제 1
# 10
# 69 42 68 76 40 87 14 65 76 81
# 50
# ▣ 출력예제 1
# 20

def flatteningFnc (n, arr, t):

    for _ in range(t):
        maxIndex = arr.index(max(arr))
        minIndex = arr.index(min(arr))
        arr[minIndex] += 1
        arr[maxIndex] -= 1

    res = max(arr)-min(arr)
    return res

def inputFnc():
    L = int(input())
    storage = list(map(int,input().split()))
    tries = int(input())

    return L,storage,tries

L, storage, tries = inputFnc()


res = flatteningFnc(L,storage,tries)
print(res)