# 그냥 단순히 2중 포문으로 그리디 갈려버리면 되긴하는데
# 이럼 시초 안당하나 20_000 * 20_000 = 400,000,000 4억이 되어 버리니까 t = 1 이라도 터짐
# 내생각엔 우선 정렬을 해야할듯 흠 약간 정렬 그리드 방식으로 풀긴했는데 이럼 시복이 어떻게 되려나
# 와 25% 까지는 맞았음 이후는 시초 뜸 ㅋ
# 으으아앙 ㅅㅂ 정렬까지 생각을 했음 이제 이분탐색을 적용할줄을 알아야지 ㅋㅋㅋ
# 봐봐 모지리야 정렬을 했어 그럼 딱 중간 지점 찍고 얘보다 크냐 작냐로 얼만큼 가져갈수 있는데 판가름이 나자나
# 값이 중간값도가 크면 중간값을 start 로 두고 다시 업다운 하는거고 반대면 반대로 하는거고 이걸 왜 몰라~
import sys

def binarySearch(x, arr):
    start, end = 0, m - 1
    res = 0

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] < x:
            res = mid + 1
            start = mid + 1
        else:
            end = mid - 1
    return res

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = sorted(list(map(int, input().split())))
        b = sorted(list(map(int, input().split())))
        cnt = 0

        for x in a:
            cnt += binarySearch(x, b)

        print(cnt)


