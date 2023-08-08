# 흠 아무리 봐도 이전에 풀었던 기타레슨 문제랑 비슷하게 가지 않을까 싶었는데 아닌듯 ㅋ
# 이건 뭐가 문제냐면 자 0에 가장 가까운 값을 목표값으로 정했어
# 근데 그 3개 용액을 어떻게 구할껀데
# 기타레슨은 무조건 순서대로 시작해야하니까 반복문 하나만 해도 퉁칠수 있는데
# 이 문제는 그렇지 않음 그냥 마구잡이로 집어서 3개 해야하는거임
# 그러면 반복문 x3 == n^3 을 매번 돌려야하는데
# 이게 브루투스 완전탐색이랑 뭐가 달라 오히려 그냥 단순히 n^3 하고 가장 0에 가까운 수 비교대입하는게 더 빠를지도 모름 ㅋ
# 그렇기에 푸는 방법이 또 있데
# 그거시 바로 3SUM 앙~고리즘 이라카데
# https://velog.io/@nkw011/baekjoon-2473

# 대에충 n*log(n) 정도 되는듯?
# for 문 i 로 하나 고정하고 i+1, n-1 를 start, end로 하나하나 좁혀가는거임
import sys

def ThreeSum():
    res = [sys.maxsize, sys.maxsize, sys.maxsize]
    for i in range(n):
        start = i + 1
        end = n - 1

        while start < end:
            tmp = arr[i] + arr[start] + arr[end]
            if abs(sum(res)) > abs(tmp):
                res = [arr[i], arr[start], arr[end]]

            if tmp == 0:
                return [arr[i], arr[start], arr[end]]

            if tmp > 0:
                end -= 1
            else:
                start += 1
    return res

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    answer = ThreeSum()
    print(*answer)

