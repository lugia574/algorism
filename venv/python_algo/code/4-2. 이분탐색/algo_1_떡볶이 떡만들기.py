# 하도 내가 이분탐색을 못하길래
# 좀 공부할겸 찾아봄
# https://www.youtube.com/watch?v=94RC-DsGMLo
# 내가 주로 헤매는 문제는 파라메트릭 서치(Parametric Search) 라는 문제로
# 최적화 문제를 결정 문제(예, 아니오)로 바꾸어 해결하는 기법

# 예시 ex) 특정 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 코테에서 파라메트릭 서치 문제는 이분탐색으로 쉽게 풀 수 있음

# 문제) 떡복이 떡 만들기
# 떡의 길이가 일정치 않아 손님이 요청한 길이가 m 일때
# 적어도 M 만큼 얻기 위해 절단기에 설정할 수 잇는 높이 최댓값을 구하라

# 여기서 핵심은 mid 값으로 할시 조건을 만족하는가? 를 확인하는 것
# 조건 만족 여부에 따라 탐색범위를 좁혀 나가는거임

def solution(n, m, arr):
    lt = 0
    answer = rt = max(arr)

    while lt <= rt:
        mid = lt + (rt - lt) // 2
        slicing = 0

        for i in range(n):
            slicing += arr[i] - mid if arr[i] > mid else 0
        if slicing == m:
            return mid
        elif slicing > m:
            lt = mid + 1
            answer = min(lt, answer)
        else:
            rt = mid - 1

    return answer

if __name__ == "__main__":
    n = 4
    m = 6
    arr = [19, 15, 10, 17]
    res = 15
    ans = solution(n, m, arr)
    print(res == ans, ans)